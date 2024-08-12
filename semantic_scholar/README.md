# Semantic Scholar Processing

This repository contains scripts and data used for processing and analyzing Semantic Scholar data. The main components include a Google Colab notebook for processing data and a JSONL file containing processed data from the Semantic Scholar corpus.

## Repository Contents

### 1. `semantic_scholar_processing.ipynb`
This Google Colab notebook contains code for processing and analyzing data from the Semantic Scholar corpus. The notebook is designed to:
- **Load**: Load the raw data including TLDR summaries, Abstracts and S2ORC metadata.
- **Preprocess**: Clean and preprocess the data, focusing on key fields such as paper titles, abstracts, and author information.
- **Transform**: Merge TLDR summaries and Abstracts with S2ORC metadata to create a comprehensive dataset, whilst reducing token usage by scoring and filtering based on TLDRs and Abstracts.
- **Score**: Calculate custom CRITERIA scores for each paper.
- **Filter**: Return only the papers with a high Relevance score.
- **Export**: Save the processed data into a JSONL file.

### 2. `final_combined_tldr_and_s2orc.jsonl`
This JSONL (JSON Lines) file contains the processed data, which is a combination of TLDR summaries and S2ORC (Semantic Scholar Open Research Corpus) data. Each line in the file represents a JSON object with fields capturing various aspects of research papers from the Semantic Scholar corpus. Please note that this file is a sample, not the entirety of the filtered dataset. We will release the full dataset filtered and ranked by relevance to veganism in the near future.

### JSON Object Example
```json
{
  "paperId": "1234567890",
  "title": "Sample Paper Title",
  "abstract": "This is a sample abstract of the paper...",
  "venue": "Sample Conference",
  "year": 2020,
  "outCitations": ["9876543210", "1122334455"],
  "inCitations": ["6677889900", "4455667788"],
  "fieldsOfStudy": ["Medicine"],
  "s2FieldsOfStudy": [
    {"category": "Medicine", "source": "external"},
    {"category": "Agricultural and Food Sciences", "source": "s2-fos-model"}
  ],
  "tldr": {
    "model": "tldr@v2.0.0",
    "text": "This is a brief summary of the paper's findings."
  },
  "publicationDate": "2020-01-17",
  "journal": {"name": "Sample Journal", "volume": "15"},
  "authors": [
    {"authorId": "91099263", "name": "A. Author"},
    {"authorId": "2094105363", "name": "B. Author"}
  ],
  "citationStyles": {
    "bibtex": "@Article{Author2020Sample,\n author = {A. Author and B. Author},\n journal = {Sample Journal},\n title = {Sample Paper Title},\n volume = {15},\n year = {2020}\n}"
  },
  "CRITERIA": {
    "CRITERIA_scores": {
      "Cultural_Sensitivity": 0.5,
      "Relevance": 0.8,
      "Insight": 0.7,
      "Trustworthiness": 0.8
    },
    "CRITERIA_final_score": 0.66
  }
}
```

## Usage

### Running the Notebook
To run the `semantic_scholar_processing.ipynb` notebook, you will need access to Google Colab. You can upload the notebook to Colab and run it step-by-step.

### Data Format
The `final_combined_tldr_and_s2orc.jsonl` file is structured such that each line contains a JSON object with metadata, TLDR summaries, author information, and custom evaluation scores for individual research papers.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/semantic-scholar-processing.git
   ```

2. Navigate to the project directory:

   ```bash
   cd semantic-scholar-processing
   ```

3. Open the notebook in Google Colab and run the cells as instructed.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions for improvements or if you find any bugs.

## License

The Semantic Scholar dataset is licences under Open Data Commons Attribution License (ODC-By) v1.0 - see the [LICENSE]([LICENSE](https://opendatacommons.org/licenses/by/1-0/)) file for full details.

In simple terms, "You are free:

To share: To copy, distribute and use the database.

To create: To produce works from the database.

To adapt: To modify, transform and build upon the database.

As long as you:

Attribute: You must attribute any public use of the database, or works produced from the database, in the manner specified in the license. For any use or redistribution of the database, or works produced from it, you must make clear to others the license of the database and keep intact any notices on the original database."

## Contact

For any questions or inquiries, please open an issue in the repository or contact the repository maintainer.
