# Open Food Facts Dataset

## Overview
The **Open Food Facts** dataset is a free, collaborative, and open database of food products from around the world. It provides detailed information about thousands of food items, including ingredients, nutritional facts, packaging, additives, allergens, and more. The dataset aims to bring transparency to food products, helping consumers make informed decisions.

## License
- **Database License:** Open Database License (ODbL)
- **Content License:** Database Contents License (DbCL)
- **Images License:** Creative Commons Attribution ShareAlike (CC BY-SA)

For full terms and conditions, visit the [Open Food Facts Terms and Conditions](https://world.openfoodfacts.org/terms-of-use).

## Data Exports

### MongoDB Dump
- **Description:** A complete dump of the Open Food Facts database in MongoDB format.
- **Link:** [Download MongoDB dump](https://static.openfoodfacts.org/data/openfoodfacts-mongodbdump.gz)
- **Checksum:**
  - [SHA256](https://static.openfoodfacts.org/data/gz-sha256sum)
  - [MD5](https://static.openfoodfacts.org/data/gz-md5sum)

### Delta Export
- **Description:** Daily exports for the previous 14 days, containing updates and changes in JSON format.
- **Link:** [View delta files](https://static.openfoodfacts.org/data/delta/index.txt)

### JSONL Data Export
- **Description:** The entire database in JSONL format, where each line is a JSON object.
- **Link:** [Download JSONL data](https://static.openfoodfacts.org/data/openfoodfacts-products.jsonl.gz)

### CSV Data Export
- **Description:** Compressed CSV file of all products, readable with spreadsheet software.
- **Link:** [Download CSV data](https://static.openfoodfacts.org/data/en.openfoodfacts.org.products.csv.gz)
- **File Details:** Compressed size: ~0.9 GB, Uncompressed size: ~9 GB, Encoding: UTF-8, Separator: Tab

### RDF Data Export
- **Description:** RDF format export for semantic web and linked data applications.
- **Link:** [Download RDF data](https://world.openfoodfacts.org/data/en.openfoodfacts.org.products.rdf.gz)

### Image Data Export
- **Description:** All product images and OCR results. Available for direct download or via AWS Open Data Program.
- **Documentation:** [Image data documentation](https://world.openfoodfacts.org/data)

## API Access

### JSON API
- **Description:** Retrieve product data by barcode.
- **Example API Call:** 
  - [API Example JSON](https://world.openfoodfacts.org/api/v2/product/737628064502.json)
  - Replace `[barcode]` with the desired product barcode.
- **Documentation:** [Open Food Facts API](https://world.openfoodfacts.org/data)

### XML API
- **Description:** XML-based API for product data retrieval.
- **Example API Call:** 
  - [API Example XML](https://world.openfoodfacts.org/api/v2/product/737628064502.xml)

## Data Usage
You are encouraged to explore and reuse this data in compliance with the licenses provided. If you are building applications or tools based on the Open Food Facts dataset, feel free to share your work with the Open Food Facts community to inspire others and gain exposure.

## SDKs and Wrappers
Open Food Facts offers SDKs for various programming languages, including Python, Java, Node.js, PHP, Swift, and more. These SDKs simplify interaction with the dataset and API.

Explore the SDKs and contribute to their development:
- [GitHub SDKs](https://github.com/openfoodfacts)

## Contributions
Open Food Facts is a community-driven project. You are welcome to contribute by submitting new data, improving the existing dataset, or developing tools and apps around the data. Join the Open Food Facts community on [Slack](https://slack.openfoodfacts.org) to discuss data, exports, and API usage.

## Contact
For any questions related to the dataset, exports, or API, you can reach out via email: [reuse@openfoodfacts.org](mailto:reuse@openfoodfacts.org).
