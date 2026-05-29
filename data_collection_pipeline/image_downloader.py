import os
import hashlib
from pathlib import Path
from urllib.parse import urlparse

import pandas as pd
import requests

def ensure_https(url: str) -> str | None:
    if url is None or (isinstance(url, float) and pd.isna(url)):
        return None

    url = str(url).strip()

    if not url:
        return None
    if url.startswith("//"):
        return "https:" + url
    if not url.startswith(("http://", "https://")):
        return "https://" + url

    return url


def make_image_id_from_url(url: str) -> str:
    return hashlib.sha1(url.encode("utf-8")).hexdigest()


def guess_ext_from_url(url: str, default: str = ".jpg") -> str:
    try:
        path = urlparse(url).path
        ext = os.path.splitext(path)[1].lower()

        if ext in {".jpg", ".jpeg", ".png", ".webp", ".gif", ".tif", ".tiff"}:
            return ext
    except Exception:
        pass

    return default


def download_one(url: str, out_path: Path, timeout: int = 30) -> bool:
    out_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        with requests.get(url, stream=True, timeout=timeout) as r:
            r.raise_for_status()

            with open(out_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=1024 * 256):
                    if chunk:
                        f.write(chunk)

        return True

    except Exception as e:
        print(f"Failed: {url} -> {e}")
        return False


def download_images_from_df(
    df: pd.DataFrame,
    url_col: str = "identifier",
    out_dir: str | Path = "images",
) -> pd.DataFrame:
    df = df.copy()
    out_dir = Path(out_dir)

    df["image_url"] = df[url_col].apply(ensure_https)

    df["image_id"] = df["image_url"].apply(
        lambda u: None if u is None else make_image_id_from_url(u)
    )

    df["file_ext"] = df["image_url"].apply(
        lambda u: None if u is None else guess_ext_from_url(u)
    )

    df["local_path"] = df.apply(
        lambda r: None
        if r["image_id"] is None
        else str(out_dir / f"{r['image_id']}{r['file_ext']}"),
        axis=1,
    )

    ok_list = []

    for url, local_path in zip(df["image_url"], df["local_path"]):
        if url is None or local_path is None:
            ok_list.append(False)
            continue

        local_path = Path(local_path)

        if local_path.exists() and local_path.stat().st_size > 0:
            ok_list.append(True)
            continue

        ok_list.append(download_one(url, local_path))

    return df