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
| https://storage.googleapis.com/open_paws_spreadsheets/WFP%20Estimates%20of%20Time%20in%20Pain%20%20-%20Hens%20-%20Time%20in%20Pain%20per%20Harm.csv | This data comes from the spreadsheet 'WFP Estimates of Time in Pain - Hens - Time in Pain per Harm'. The fields are described as follows: 'Animal / Study' is Laying Hens, 'Scenario' is Cage-free, 'Harm Nature' is Psychological, 'Category of Challenge' is Behavioral Deprivation, 'Challenge' is Roosting at Elevated Area, 'Intensity' is Annoying, 'Time Unit' is hour, 'Mean time in pain' (spent by 'average' population member, takes harm prevalence into account) is 74.81, 'Lower bound' is 44.54, 'Upper bound' is 105.08, 'Mean time in pain' (spent by 'affected' individual, does not consider population prevalence) is 498.75, 'Lower bound.1' is 440.63, 'Upper bound.1' is 556.87. | text   | 199      |

### Link to the Dataset

You can access the dataset using the following link: [Download Dataset](https://drive.google.com/file/d/1-0I8sytFjQiN0LyPPCXq8lvKiuBXHF_u/view?usp=drive_link)
