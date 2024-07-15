# Open Assistant Dataset Filtering

This folder contains scripts for filtering the Open Assistant dataset based on the CRITERIA score and the final file containing messages filtered for relevance to veganism and/or animal rights. 

The goal is to create a refined dataset that is relevant to veganism and animal rights while maintaining the structure and quality necessary for AI training.

## Files and Scripts

### `oasst2_criteria_ranking.ipynb`
This Google Colab files assigns a CRITERIA score to each message in the dataset. The CRITERIA score helps in evaluating the content's relevance and quality.

### `merge_jsonl.py`
This script is used to merge files that have been augmented with a CRITERIA score into a single dataset.

### `filter_oasst2.py`
This script filters the Open Assistant dataset based on the CRITERIA score.

### `oasst2_filtered.jsonl`
This is the final file containing all filtered messages stored within message trees, including their CRITERIA scores.

## Open Assistant Dataset Details

### Project and License

The Open Assistant Conversations dataset aims to democratize research on large-scale alignment of large language models (LLMs) by providing a human-generated, human-annotated assistant-style conversation corpus. This project is supported by a worldwide crowd-sourcing effort involving over 13,500 volunteers.

### License
All data in this folder is open source under permissive licenses such as Apache 2.0 or MIT. Any data added by contributors must also include a permissive license. In cases where data was scraped or existing datasets were used, proof of the permissive license must be included. For human-generated data, proof of permission must be included.

### Reference Paper
The Open Assistant Conversations dataset is detailed in the following paper:

**Title:** OpenAssistant Conversations -- Democratizing Large Language Model Alignment  
**Authors:** Andreas Köpf, Yannic Kilcher, Dimitri von Rütte, Sotiris Anagnostidis, Zhi-Rui Tam, Keith Stevens, Abdullah Barhoum, Nguyen Minh Duc, Oliver Stanley, Richárd Nagyfi, Shahul ES, Sameer Suri, David Glushkov, Arnav Dantuluri, Andrew Maguire, Christoph Schuhmann, Huu Nguyen, Alexander Mattick  
**Comments:** Published in NeurIPS 2023 Datasets and Benchmarks  
**Subjects:** Computation and Language (cs.CL); Artificial Intelligence (cs.AI)  
**Cite as:** arXiv:2304.07327 [cs.CL]  
**DOI:** [https://doi.org/10.48550/arXiv.2304.07327](https://doi.org/10.48550/arXiv.2304.07327)

### Open Assistant Conversations Dataset Release 2 (OASST2)
This dataset contains message trees collected from the open-assistant.io website until November 5, 2023. Each message tree has an initial prompt message as the root node, which can have multiple child messages as replies, and these child messages can have multiple replies.

#### Dataset Structure
- **Roles**: Each message has a role property, which can be either "assistant" or "prompter". The roles alternate between "prompter" and "assistant" in conversation threads.
- **Data Collection Period**: The dataset includes data collected up to November 5, 2023.

#### JSON Example: Original Message (without CRITERIA score)
For readability, the following JSON example is formatted with indentation. In actual jsonl files, objects are stored without indentation.

```json
{
    "message_id": "218440fd-5317-4355-91dc-d001416df62b",
    "parent_id": "13592dfb-a6f9-4748-a92c-32b34e239bb4",
    "user_id": "8e95461f-5e94-4d8b-a2fb-d4717ce973e4",
    "text": "It was the winter of 2035, and artificial intelligence (..)",
    "role": "assistant",
    "lang": "en",
    "review_count": 3,
    "review_result": true,
    "deleted": false,
    "rank": 0,
    "synthetic": true,
    "model_name": "oasst-sft-0_3000,max_new_tokens=400 (..)",
    "labels": {
        "spam": { "value": 0.0, "count": 3 },
        "lang_mismatch": { "value": 0.0, "count": 3 },
        "pii": { "value": 0.0, "count": 3 },
        "not_appropriate": { "value": 0.0, "count": 3 },
        "hate_speech": { "value": 0.0, "count": 3 },
        "sexual_content": { "value": 0.0, "count": 3 },
        "quality": { "value": 0.416, "count": 3 },
        "toxicity": { "value": 0.16, "count": 3 },
        "humor": { "value": 0.0, "count": 3 },
        "creativity": { "value": 0.33, "count": 3 },
        "violence": { "value": 0.16, "count": 3 }
    }
}

#### JSON Example: Filtered Message (with CRITERIA score)
For readability, the following JSON example is formatted with indentation. In actual jsonl files, objects are stored without indentation.

{
    "message_tree_id": "21bc9a3e-3a6c-4d82-9e50-d73b52d9b359",
    "tree_state": "prompt_lottery_waiting",
    "prompt": {
        "message_id": "21bc9a3e-3a6c-4d82-9e50-d73b52d9b359",
        "parent_id": null,
        "user_id": "f7fdb076-f6c2-4b66-957c-efaaf91fe3b2",
        "created_date": "2023-02-15T23:58:42.359930+00:00",
        "text": "“The question is not, Can they reason?, nor Can they talk? but, Can they suffer? Why should the law refuse its protection to any sensitive being?”  Can you explain what this quote from Jeremy Bentham means?",
        "role": "prompter",
        "lang": "en",
        "review_count": 3,
        "review_result": true,
        "deleted": false,
        "rank": null,
        "synthetic": false,
        "model_name": null,
        "emojis": {"-1": 1, "_skip_labeling": 1},
        "replies": [],
        "labels": {
            "spam": {"value": 0.0, "count": 3},
            "lang_mismatch": {"value": 0.0, "count": 3},
            "pii": {"value": 0.0, "count": 3},
            "not_appropriate": {"value": 0.0, "count": 3},
            "hate_speech": {"value": 0.0, "count": 3},
            "sexual_content": {"value": 0.0, "count": 3},
            "quality": {"value": 0.5833333333333334, "count": 3},
            "toxicity": {"value": 0.08333333333333333, "count": 3},
            "humor": {"value": 0.08333333333333333, "count": 3},
            "creativity": {"value": 0.5, "count": 3},
            "violence": {"value": 0.0, "count": 3}
        },
        "events": null,
        "detoxify": {
            "toxicity": 0.00041286207851953804,
            "severe_toxicity": 1.7660802768659778e-05,
            "obscene": 0.00011150849604746327,
            "identity_attack": 6.814768130425364e-05,
            "insult": 0.00018772293697111309,
            "threat": 2.4862520149326883e-05,
            "sexual_explicit": 2.0736444639624096e-05
        },
        "message_tree_id": null,
        "tree_state": null,
        "CRITERIA": {
            "Cultural_Sensitivity": 0.5,
            "Relevance": 1.0,
            "Insight": 0.8,
            "Trustworthiness": 1.0,
            "Emotional_Impact": 0.6,
            "Rationality": 1.0,
            "Influence": 0.8,
            "Alignment": 1.0,
            "CRITERIA_final_score": 0.84
        }
    },
    "origin": null
}
