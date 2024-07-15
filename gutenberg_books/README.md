# Project Gutenberg Text Chunks

This folder contains manually selected books on Project Gutenberg that are relevant to animal rights and plant-based diets, divided into text chunks which are labelled by their position in the book. These texts have been chosen to provide domain-specific data for collecting human feedback from animal advocates. It should be noted that many of these books are focused on vegetarianism rather than veganism, or about domesticated animals more generally rather than specifically from a pro-animal perspective. Therefore, it should be used primarily for gathering human feedback rather than directly for training AI or ML models.

## Project and License

Project Gutenberg is a valuable resource for public domain books. Most of the eBooks on Project Gutenberg are in the public domain in the United States, meaning they can be used freely, including for commercial purposes. For more information, please refer to the [Project Gutenberg Terms of Use](https://www.gutenberg.org/policy/permission.html).

### License
All data in this folder is sourced from Project Gutenberg and is in the public domain. This means no permission is needed for its use, and it can be freely redistributed and modified.

## Files and Scripts

### `gutenberg_books_text_chunks.csv`
This file contains chunks of text from various books, selected for their relevance to animal rights and plant-based diets. The books themselves were manually selected by searching for terms including vegetarianism, animal rights, and animal welfare. The chunks were then scraped using Octoparse, a no-code web scraping tool.

### CSV Structure
The CSV file is structured with the following columns:
- `Website_URL`: The URL of the book on Project Gutenberg.
- `Title`: The title of the book.
- `Author`: The author of the book.
- `Date`: The publication date of the book.
- `Language`: The language of the text chunk.
- `Text_Chunk`: The selected chunk of text.
- `Position`: The position of the text chunk within the book.
