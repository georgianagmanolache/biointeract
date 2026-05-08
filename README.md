# BioInteract: A Large-Scale Multimodal Dataset for Evaluating Fine-Grained Semantic Understanding of Biotic Interactions

We present [BioInteract](https://huggingface.co/datasets/BioInteract/BioInteract), a large-scale multimodal dataset that exposes limitations in fine-grained semantic understanding of biotic interactions—directional relationships between organisms whose meaning depends on subtle semantic cues.

While recent advances in vision–language models (VLMs) have spurred the development of domain-specific datasets and benchmarks, these often fail to assess fine-grained semantic understanding, allowing models to achieve high scores without robust visual grounding. We address this evaluation gap through the lens of biotic interactions: directional, asymmetric relationships between organisms (e.g., wasp parasitizes caterpillar vs. caterpillar parasitizes wasp).
We further introduce `BioInteract100`, an adversarial image retrieval benchmark revealing that state-of-the-art VLMs suffer from severe consistency gaps and are highly brittle to relation-direction reversals.

## Dataset

Curated from iNaturalist and validated against scientific literature, `BioInteract` contains 15.4K unique interactions spanning 6.5K taxa across 256K images. Each interaction is structured as a source-relation-target triplet, enabling controlled semantic perturbations.

Data is available via [HuggingFace](https://huggingface.co/datasets/BioInteract/BioInteract).

## Evaluation

### Models

We evaluate CLIP-style models for text-to-image retrieval, such as [OpenAI](https://huggingface.co/openai/clip-vit-large-patch14), [MetaCLIP] (https://huggingface.co/facebook/metaclip-2-worldwide-huge-quickgelu), [SigLIP](https://huggingface.co/timm/ViT-SO400M-14-SigLIP), [SigLIP2](https://huggingface.co/timm/ViT-L-16-SigLIP2-256), as well as specialized models, such as [BioTrove-CLIP-B](https://huggingface.co/BGLab/BioTrove-CLIP), [BioCAP](https://huggingface.co/imageomics/biocap), [BioCLIP](https://huggingface.co/imageomics/bioclip), and [BioCLIP2](https://huggingface.co/imageomics/bioclip-2).
We adopt proprietary multimodal language models (MLLMs) such as [GPT-5.4 mini](https://developers.openai.com/api/docs/models/gpt-5.4-mini), [Claude Sonnet 4.6](https://www.anthropic.com/claude/sonnet), and [Gemini 3 Flash Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview) for ranking prompting for each image and corresponding queries per image: `Does this image show {some query}? Answer with "Yes" or "No" and nothing else`. All proprietary models were evaluated via their APIs with deterministic decoding `temperature=0.0`.

| Name | Model URL |
| --- | --- | 
| OpenAI | [https://huggingface.co/openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) |
| MetaCLIP | [https://huggingface.co/facebook/metaclip-2-worldwide-huge-quickgelu](https://huggingface.co/facebook/metaclip-2-worldwide-huge-quickgelu) |
| SigLIP | [https://huggingface.co/timm/ViT-SO400M-14-SigLIP](https://huggingface.co/timm/ViT-SO400M-14-SigLIP) |
| SigLIP2 | [https://huggingface.co/timm/ViT-L-16-SigLIP2-256](https://huggingface.co/timm/ViT-L-16-SigLIP2-256) |
| BioTrove-CLIP-B | [https://huggingface.co/BGLab/BioTrove-CLIP](https://huggingface.co/BGLab/BioTrove-CLIP) | 
| BioCAP | [https://huggingface.co/imageomics/biocap](https://huggingface.co/imageomics/biocap) |
| BioCLIP | [https://huggingface.co/imageomics/bioclip](https://huggingface.co/imageomics/bioclip) | 
| BioCLIP2 | [https://huggingface.co/imageomics/bioclip-2](https://huggingface.co/imageomics/bioclip-2) | 
| GPT-5.4 mini | [https://developers.openai.com/api/docs/models/gpt-5.4-mini](https://developers.openai.com/api/docs/models/gpt-5.4-mini) |
| Gemini 3 Flash Preview | [https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview) | 
| Claude Sonnet 4.6 | [https://www.anthropic.com/claude/sonnet](https://www.anthropic.com/claude/sonnet) | 

## Acknowledgments
Parts of this project page were adopted from the [Nerfies](https://nerfies.github.io/) page.

## Website License
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
