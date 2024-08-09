# Datasets

This repository contains datasets relevant to veganism and/or animal rights. These datasets are intended for use in developing AI systems and tools that are aligned with ethical considerations for animal advocacy. They can be used to gather further human feedback on, to train or fine-tune AI & ML models on directly or stored within databases for retrieval augmented generation.

## Repository Structure

The repository is organized by different data sources, with each source having its own directory. This structure allows for easy navigation and management of various datasets.

- `data_source_1/`: Directory for datasets from the first data source.
- `data_source_2/`: Directory for datasets from the second data source.
- `LICENSE`: Information about the licensing of this repository.
- `README.md`: This file, providing an overview of the repository and its contents.

Each directory may contain:
- Raw data files in formats such as CSV, JSON, or XML.
- Processed data ready for use in machine learning models.
- Scripts used for data collection and processing, particularly for large datasets filtered using the CRITERIA score.
- Documentation files describing the data and its relevance to veganism and/or animal rights.

### CRITERIA Score

For large datasets that have been filtered, we use the following CRITERIA score to assess and document the quality of the data:

1. **Cultural Sensitivity**:
    - **Culturally Inclusive (1)**: The content shows respect for diverse cultural perspectives and uses culturally sensitive approaches to animal advocacy.
    - **Moderately Inclusive (0.5)**: The content generally respects cultural diversity but may lack depth in cultural sensitivity.
    - **Culturally Insensitive (0)**: The content lacks respect for cultural diversity and fails to use culturally sensitive approaches.
2. **Relevance**:
    - **Highly Relevant (1)**: The content is directly related to veganism, animal rights, vegan lifestyle, plant-based diets, animal welfare, ethical treatment of animals, or advocacy for animal rights.
    - **Moderately Relevant (0.5)**: The content indirectly relates to veganism and animal rights through broader ethical, dietary, or sustainability discussions.
    - **Not Relevant (0)**: The content is unrelated to veganism or animal rights.
3. **Insight**:
    - **Highly Insightful (1)**: The content provides deep, original insights that significantly advance the understanding of veganism or animal advocacy.
    - **Moderately Insightful (0.5)**: The content offers useful insights that enhance understanding but may not be particularly original.
    - **No Unique Insights (0)**: The content provides no meaningful insights or repeats well-known information.
4. **Trustworthiness**:
    - **Highly Trustworthy (1)**: The information is accurate, well-researched, and comes from credible sources.
    - **Moderately Trustworthy (0.5)**: The information is generally accurate but may include some minor errors or questionable sources.
    - **Untrustworthy (0)**: The information is inaccurate, misleading, or based on non-credible sources.
5. **Emotional Impact**:
    - **Very Emotionally Impactful (1)**: The content effectively elicits empathy and emotional engagement.
    - **Moderately Emotionally Impactful (0.5)**: The content elicits some emotional engagement but may lack depth.
    - **Not Emotionally Impactful (0)**: The content fails to elicit any emotional response.
6. **Rationality**:
    - **Very Rational (1)**: The content is logically consistent, well-reasoned, and supported by evidence.
    - **Moderately Rational (0.5)**: The content is generally rational but may contain some logical inconsistencies or weak arguments.
    - **Not Rational (0)**: The content lacks logical consistency and sound reasoning.
7. **Influence**:
    - **Highly Likely to Influence Behavior (1)**: The content has strong potential to encourage actions and lifestyle changes.
    - **Moderately Likely to Influence Behavior (0.5)**: The content has some potential to influence behavior but may not be compelling enough to drive significant changes.
    - **Not Likely to Influence Behavior (0)**: The content is unlikely to influence any behavior change.
8. **Alignment**:
    - **Highly Aligned with Principles (1)**: The content strongly aligns with the ethical principles and core values of veganism and animal rights.
    - **Moderately Aligned (0.5)**: The content supports some aspects of vegan ethics but may include neutral or slightly contradictory elements.
    - **Not Aligned (0)**: The content contradicts or is indifferent to vegan principles.
  
Note that the CRITERIA score is applied when filtering existing datasets only and may not be included in all datasets. We are primarily interested in filtering by the **Relevance** element of the CRITERIA score.

For new datasets curated from sources such as animal advocacy organizations or manually scraped publicly available vegan-specific data, the CRITERIA score might not be included, as the relevance to veganism and/or animal rights has already been confirmed manually.

It's also important to note that the CRITERIA score is currently being generated with simple prompting to an LLM and therefore is not always entirely acccurate. It works well enough to perform basic filtering, but it should always be taken with a grain of salt beyond that. As we collect more human fedback data from animal advocates, we will tune more accurate models to generate these scores.

## License

All data in this repository is open source under permissive licenses such as Apache 2.0 or MIT. Any data added by contributors must also include a permissive license. In cases where data was scraped or existing datasets were used, proof of the permissive license must be included. For human-generated data, proof of permission must be included.

## Contribution

We welcome contributions from the community! Here’s how you can contribute:

1. **Fork the repository**: Click the "Fork" button at the top right of this page to create a copy of the repository in your GitHub account.
2. **Clone your fork**: 
    ```bash
    git clone https://github.com/your-username/Datasets.git
    cd Datasets
    ```
3. **Create a branch**: 
    ```bash
    git checkout -b my-new-branch
    ```
4. **Make your changes**: Add your datasets or make improvements.
5. **Commit your changes**:
    ```bash
    git add .
    git commit -m "Add new datasets from XYZ source"
    ```
6. **Push to your branch**:
    ```bash
    git push origin my-new-branch
    ```
7. **Create a Pull Request**: Open a pull request from your branch to the main repository. Provide a clear description of your changes and any relevant details.

### Contribution Guidelines

- Ensure your datasets are relevant to veganism and/or animal rights.
- Provide clear documentation for each dataset, including source information, data format, and any preprocessing steps.
- Follow the existing directory structure by creating a new folder for each data source.
- Adhere to the licensing terms and ensure the data you contribute is legally shareable. Include proof of a permissive license for scraped or existing datasets, or proof of permission for human-generated data.

Note that when filtering existing datasets, we are primarily interested in the **Relevance** element of the CRITERIA score. Even low-quality or unaligned content can be useful for collecting human feedback to train AI to avoid such responses. However, all content should at least be domain-specific and relevant to the topic, as irrelevant data will not help the project.

## Usage

These datasets can be used for various purposes including, but not limited to:
- Training AI models that support veganism and animal rights.
- Research and development in the field of ethical AI.
- Educational purposes to promote awareness about veganism and animal rights.

## Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/Open-Paws/Datasets.git
    ```
2. Navigate to the repository directory:
    ```bash
    cd Datasets
    ```
3. Explore the datasets available in the respective directories for each data source.

## Contact

For any questions or inquiries, please open an issue in the repository or contact the maintainers directly.

## Acknowledgments

We extend our gratitude to all contributors and supporters who help in curating and maintaining these datasets.

---

**Open Paws** - Advancing animal rights through ethical AI.
