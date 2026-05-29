from pathlib import Path

import pandas as pd

from image_downloader import download_images_from_df

PARQUET_FILE = "icun.parquet"
OUT_DIR = "images"
URL_COL = "identifier"


def main():
    df = pd.read_parquet(PARQUET_FILE)

    Path(OUT_DIR).mkdir(parents=True, exist_ok=True)

    df = download_images_from_df(
        df=df,
        url_col=URL_COL,
        out_dir=OUT_DIR,
    )

    df.to_parquet(PARQUET_FILE, index=False)

    print(f"Saved updated parquet to: {PARQUET_FILE}")
    print(f"Images saved in: {OUT_DIR}")
    print(f"Downloaded OK: {df['download_ok'].sum()} / {len(df)}")


if __name__ == "__main__":
    main()