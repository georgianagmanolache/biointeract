# Evaluating CLIP-style on species interaction recognition

This repository contains scripts and datasets for evaluating CLIP-style vision-language models (VLMs) on their ability to recognize ecological species interactions from images.

## Task description

For image retrieval, each image in the evaluation set is encoded into a fixed-dimensional embedding vector. Text descriptions corresponding to ecological species interactions are encoded into the same embedding space. Retrieval performance is then evaluated by ranking images according to their similarity to a given text query.

Given a query describing a species interaction (e.g., "a bee pollinating a flower" or "a spider preying on an insect"), cosine similarity is computed between the text embedding and all image embeddings. Images are ranked by similarity score, and retrieval metrics such as Recall@K, Median Rank, and Mean Reciprocal Rank (MRR) can be computed to assess how effectively the model associates visual evidence with ecological interaction concepts.

The generated image embeddings are stored and reused during evaluation, enabling efficient large-scale retrieval experiments without repeatedly processing the images through the vision encoder.


## Data preparation

The notebook `imgage_embeddimgs.ipynb` prepares the evaluation datasets and generates the image embeddings for each image.


