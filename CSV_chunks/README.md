# Dataset: Text and Metadata Extracted from Spreadsheets on Veganism and Animal Rights

This dataset contains structured data extracted from spreadsheets that focus on veganism, animal rights, and related topics. The data has been organized into natural language descriptions to make it more accessible for analysis and machine learning projects.

## Dataset Description

- **Source**: Various spreadsheets containing data relevant to veganism, animal rights, and welfare considerations.
- **Data Type**: Textual descriptions based on the extracted spreadsheet data.
- **File Format**: Content is provided in a structured format that outlines the details and metadata of each spreadsheet entry.

### Structure of the Dataset

The dataset is organized into the following columns:

| Column    | Description                                                                                                 |
|-----------|-------------------------------------------------------------------------------------------------------------|
| `url`     | The URL of the spreadsheet from which the data was extracted.                                                |
| `content` | A natural language description of the spreadsheet data, detailing the contents of each relevant cell.        |
| `type`    | The type of the content extracted: typically `text` to indicate the data has been converted to a narrative.  |
| `position`| The position of the content chunk in the spreadsheet, indicating the order in which it appears.              |

### Example of Dataset Entries

Below is an example of how the data might look within the dataset:

| url                                                                                       | content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | type   | position |
|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|----------|
| https://storage.googleapis.com/open_paws_spreadsheets/AJ%20WFM_.xlsx                      | This data comes from the spreadsheet 'AJ WFM_'. The fields are described as follows: 'ASK IDEA' is not available, 'Unnamed: 2' is not available, 'Unnamed: 3' is TOTAL, 'STRENGTH OF IDEA' is WELFARE ESTIMATE, 'Unnamed: 5' is EVIDENCE BASE, 'Unnamed: 6' is THEORY OF CHANGE, 'PROBABILITY OF SUCCESS' is OTHER INDICATIONS THE ASK MIGHT SUCCEED, 'Unnamed: 8' is POLITICAL FEASIBILITY, 'Unnamed: 9' is PUBLIC SUPPORT, 'EXTERNALITIES' is not available, 'CRUCIAL CONSIDERATIONS' is DOES THIS PASS CRUCIAL CONSIDERATIONS? (NO = AT LEAST 1 CRUCIAL CONSIDERATION FAILED), '/ OVERALL THOUGHTS' is not available, 'SOURCE 1', 'SOURCE 2', and 'SOURCE 3' are not available. | text   | 1        |

### Link to the Dataset

You can access the dataset using the following link: [Download Dataset](https://drive.google.com/file/d/1-0I8sytFjQiN0LyPPCXq8lvKiuBXHF_u/view?usp=drive_link)
