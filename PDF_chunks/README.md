# Dataset: Text and Image Chunks Extracted from PDFs on Veganism and Animal Rights

This dataset contains extracted text and image data from several PDFs that focus on topics related to veganism, animal rights, and animal welfare. The content has been processed to provide structured chunks of textual and visual information suitable for analysis, research, and machine learning projects.

## Dataset Description

- **Source**: Various PDFs focused on veganism, animal rights, ethics, and related topics.
- **Data Type**: Both text and image data extracted from the source PDFs.
- **File Format**: Text content is stored in structured formats, and images are saved in standard image formats (e.g., PNG, JPEG).

### Structure of the Dataset

The dataset is organized into the following columns:

| Column    | Description                                                                                                                      |
|-----------|----------------------------------------------------------------------------------------------------------------------------------|
| `url`     | The URL of the source PDF from which the content was extracted.                                                                  |
| `content` | The text chunk extracted from the PDF. This can be sentences, paragraphs, or sections containing information about veganism and animal rights. |
| `type`    | The type of the content extracted: either `text` for textual data or `image` for visual data.                                    |
| `position`| The position of the content chunk in the document, indicating the order in which it appears.                                      |

### Example of Dataset Entries

Below is an example of how the data might look within the dataset:

| url                                                                                       | content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | type   | position |
|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|----------|
| https://storage.googleapis.com/open_paws_pdfs/1311-JBS-NOIE-101918.pdf                    | "USDA... United States Department of A!':iriculture Food Safety and Inspection Service Office of Field Operations Philadelphia District Mellon Independence Center, 701 Market Street Suite 4100-A Philadelphia, PA 19106 October 19, 2018 Mr. Michael Cox, General Plant Manager JBS Souderton, Inc. (Est. 1311) 249 Allentown Road Souderton, PA 18964 NOTICE OF INTENDED ENFORCEMENT Dear Mr. Cox, This letter confirms verbal notification provided to you, Plant Manager, by Mr. Joseph Schein, Deputy District Manager (DDM), at approximately 8:35 A.M. on October 19, 2018..." | text   | 1        |
| https://storage.googleapis.com/open_paws_pdfs/animal-rights-chart-2020.pdf                | Image containing a chart that illustrates the increase in global veganism trends from 2010 to 2020.                                                                                                                | image  | 3        |

### Link to the Dataset

You can access the dataset using the following link: [Download Dataset](https://drive.google.com/file/d/1iGFOnPEvcNmSpPE-YZmBT9a8qfrH1wvd/view?usp=drive_link)
