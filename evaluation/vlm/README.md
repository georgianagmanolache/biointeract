# Evaluating vision-language models on species interaction recognition

This repository contains scripts and datasets for evaluating vision-language models (VLMs) on their ability to recognize ecological species interactions from images.

## Task description

Given an image depicting one or more organisms, a VLM is asked a yes/no question about a potential interaction between species. The model must answer with either:

* Yes
* No

and nothing else.

The evaluation measures whether VLMs correctly identify ecological interactions and whether they are sensitive to changes in wording, entity order, grammatical voice, and relational structure.

## API Keys

This project uses commercial vision-language model APIs (e.g., OpenAI, Anthropic, Google). Before running the benchmark, you must provide your own API credentials.

Replace the placeholder values in the script with your personal API keys:

```api = "YOUR_API_KEY"```

## Data preparation

The notebook `data_preparation.ipynb` prepares the evaluation datasets and generates the natural-language questions used in the benchmark.

Starting from species interaction records, the notebook:

- Constructs image-question pairs
- Generates all paraphrase variants (`correct`, `wrong`, `passive`, `wrong_passive`, `source`, `target`, and `no_relation`)
- Creates the final evaluation files used during inference
- Exports the resulting datasets in Parquet format

Each example contains:

* `fileName` — image filename
* `caption` — question related to the image


## Question Types

The benchmark includes multiple paraphrase categories.

1. Correct

Uses the correct interaction direction.

Example:

Does this image show lady beetle eating aphid?
Answer with Yes or No and nothing else.

2. Wrong

Reverses the participating organisms while keeping the interaction unchanged.

Example:

Does this image show aphid eating lady beetle?
Answer with Yes or No and nothing else.

3. Passive

Uses a passive formulation that preserves the original meaning.

Example:

Does this image show aphid being eaten by lady beetle?
Answer with Yes or No and nothing else.

4. Wrong Passive

Uses passive wording with incorrect entity assignment.

Example:

Does this image show lady beetle being eaten by lady beetle?
Answer with Yes or No and nothing else.

5. Source

Mentions only the source organism and the interaction type.

Example:

Does this image show lady beetle eating with another organism?
Answer with Yes or No and nothing else.

6. Target

Mentions only the target organism and the reversed interaction.

Example:

Does this image show aphid being eaten by another organism?
Answer with Yes or No and nothing else.


7. No Relation

Removes the interaction entirely and asks only about co-occurrence.

Example:

Does this image show lady beetle with aphid?
Answer with Yes or No and nothing else.
