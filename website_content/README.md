# Website Content Collection

This folder contains a curated collection of various types of content from websites relevant to animal rights, veganism, and plant-based diets. The content includes blogs, news articles, and other web pages, all of which have been divided into chunks, labeled by their position in the original content.

## Project and License

The content included in this collection has been sourced from various online publications, blogs, and media platforms, mostly from animal advocacy organizations and businesses run by animal advocates. All website owners have opted in and signed data-sharing agreements, agreeing for us to use this content in our database. This ensures that the data is ethically sourced and can be used freely within AI & ML applications.

## CSV Structure

The CSV files are structured with the following columns:

- **URL**: The URL of the original content.
- **Content**: The selected chunk of content (text or image URL).
- **Type**: The type of content (e.g., text or image).
- **Position**: The position of the content chunk within the original document (in this case, each URL is treated as a unique document).

### Example CSV Structure

| url                                                                                   | content                                                                                                                                                 | type  | position |
|---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-------|----------|
| https://www.openpaws.ai/research-and-reports/literature-review-on-developing-artificial-intelligence-to-advocate-for-animal-rights | https://images.squarespace-cdn.com/content/v1/6633b105dd35f079e9410acb/5b472403-9a83-4ba8-93d9-ecff205306b5/OP+White+No+Background.png?format=1500w | image | 1        |

This structure ensures that all types of content are categorized and labeled effectively for use in AI & ML applications.

## Website Scraping Script

To facilitate the creation of similar datasets from any website, we provide a script titled `website_content_scraping.ipynb` and another titled `url_content_scraping.ipynb`. These Google Colab notebooks allows users to scrape and process content from specified websites, organizing the data into the structured CSV format described above. The website content scraping script will first crawl all internal links for a given base URL and then scrape all of the URLs it finds, whereas the URL content scraping script scrapes from a given list of URLs. We recommend using the website content scraping script first, and then if there were any URLs that were unable to be scraped due to network issues or bot detection software, you can try those failed URLs again using the URL scraping script.

### Features of the Script

- **Content Extraction**: Extracts various types of content (text, images, etc.) from specified websites.
- **Content Chunking**: Divides the content into manageable chunks, labeling each chunk by its position within the original content.
- **CSV Output**: Outputs the extracted and chunked content into a CSV file, following the specified structure.

### How to Use the Script

1. **Open Google Colab**: Go to [Google Colab](https://colab.research.google.com/).
2. **Upload the Script**: Upload the `website_scraping.ipynb` file to your Google Colab environment.
3. **Configure**: Update the script with the URLs of the websites you wish to scrape.
4. **Run**: Execute the cells in the notebook to scrape the content and generate the CSV file.

By using this script, you can expand the dataset with additional content from other relevant websites, maintaining the consistency and structure needed for AI & ML applications.

### Download Datasets

[Download CSV files from Google Drive here](https://drive.google.com/drive/folders/1uW3fpVzYftOkhiF4Npm4mbFZun02-7Eb?usp=drive_link_
