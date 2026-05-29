# Data collection pipeline

Data is sourced from GloBI (Global Biotic Interactions, [https://globalbioticinteractions.org](https://globalbioticinteractions.org)) Community on Zendo and GBIF (Global Biodiversity Information Facility, [https://www.gbif.org/](https://www.gbif.org/)).

## Datasets

To be able to generate the BioInteract dataset, the following data sources are required:

| Name | Dataset URL | File |
| --- | --- | --- |
| GloBI  | [10.5281/zenodo.14640564](https://zenodo.org/records/14640564/files/interactions.csv.gz?download=1) | interactions.csv.gz |
| GBIF Backbone Taxonomy  | [https://www.gbif.org/dataset/d7dddbf4-2cf0-4f39-9b2a-bb099caae36c](https://hosted-datasets.gbif.org/datasets/backbone/current/backbone.zip) | backbone.zip |
| GBIF iNaturalist Research-grade Observations | [https://www.gbif.org/occurrence/download/0053610-251120083545085](https://www.gbif.org/occurrence/download/0053610-251120083545085) |  0053610-251120083545085.zip |

**Note:** These datasets are large and therefore not included in the repo. they need to be dowloaded before running the pipeline.

More data will be added over time as collection/annotation continues. The pipeline thus can be applied to updated resources.

## How to get BioInteract

Run the following files step by step:

1) interaction_data_collection.ipynb

2) interaction_data_validation.ipynb

3) image_downloader.ipynb



