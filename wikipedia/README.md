# Wikipedia Filtered Dataset

This folder contains scripts for filtering the Wikipedia dataset based on the CRITERIA score and the final file containing messages filtered for relevance to veganism and/or animal rights.

The goal is to create a refined dataset that is relevant to veganism and animal rights while maintaining the structure and quality necessary for AI training.

## Files and Scripts

### wiki-criteria-ranking.ipynb

This Google Colab file assigns a CRITERIA score to each chunk in the dataset. The CRITERIA score helps in evaluating the content's relevance and quality.

### filter_wiki.py

This script merges processed files and then filters those files based on the relevance aspect of the CRITERIA score.

### simple_wiki_sample.jsonl

This is the final file containing filtered Wikipedia chunks stored with their CRITERIA scores. It includes approximately half of the "simple" version of Wikipedia. Full versions in various languages will be released soon.

## Wikipedia Dataset Details

The Wikipedia dataset is derived from the [Cohere Wikipedia dataset](https://huggingface.co/datasets/Cohere/wikipedia-22-12) and includes pre-processed chunks ranked by the CRITERIA score for relevance to veganism.

Most of Wikipedia's text and many of its images are co-licensed under the Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA) and the GNU Free Documentation License (GFDL) (unversioned, with no invariant sections, front-cover texts, or back-cover texts).

Therefore, permission is granted to copy, distribute and/or modify Wikipedia's text under the terms of the Creative Commons Attribution-ShareAlike 4.0 International License and, unless otherwise noted, the GNU Free Documentation License, unversioned, with no invariant sections, front-cover texts, or back-cover texts.

### JSON Example: Filtered Chunk (with CRITERIA score)

For readability, the following JSON example is formatted with indentation. In actual jsonl files, objects are stored without indentation.

```json
{
    "id": 109,
    "title": "Global warming",
    "text": "When people burn fossil fuels like coal, oil and natural gas this adds carbon dioxide into the air. This is because fossil fuels contain lots of carbon and burning means joining most of the atoms in the fuel with oxygen. When people cut down many trees (deforestation), this means less carbon dioxide is taken out of the atmosphere by those plants. Animals which have four places in their stomachs, like cows and sheep, also cause global warming, because their burps contain a greenhouse gas called methane.",
    "url": "https://simple.wikipedia.org/wiki?curid=7368",
    "wiki_id": 7368,
    "views": 1399.0238037109375,
    "paragraph_id": 2,
    "langs": 147,
    "CRITERIA": {
        "CRITERIA_scores": {
            "Cultural_Sensitivity": 0.5,
            "Relevance": 0.7,
            "Insight": 0.4,
            "Trustworthiness": 0.8,
            "Emotional_Impact": 0.2,
            "Rationality": 0.8,
            "Influence": 0.5,
            "Alignment": 0.7
        },
        "CRITERIA_final_score": 0.5625,
        "language": "en"
    }
}
