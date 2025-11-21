**PubMed Article Downloader**

This Python program allows you to search PubMed for recent articles using Boolean ('AND'& 'OR') queries (e.g., “CRISPR AND E. coli”, “gene editing OR CRISPR”). It downloads key metadata (title, authors, publication date, source journal, and PMID) for the most recent articles matching your query, and saves the results as a CSV file to any location on your local computer.

*Features*
- Searches PubMed via the NCBI E-utilities API ([NCBI PubMed](https://pubmed.ncbi.nlm.nih.gov/) | [NCBI E-utilities API](https://www.ncbi.nlm.nih.gov/books/NBK25499/))
- Supports Boolean operators `AND` / `OR` in queries
- Results sorted by publication date (most recent first)
- User chooses save location; filename includes a timestamp to avoid overwriting
- Only requires the `requests` Python package
- A separate logic file and a main file with user interface has been created

## Usage

1.Import requests
2. Run `main.py` (user interface)
3. Enter your search query (e.g., `CRISPR AND E. coli`)
4. Enter how many articles to fetch 
5. Enter the desired folder path to save the CSV file 
6. The metadata file is saved with a timestamp to avoid filename clashes

## Dependencies
import requests
in the command line type
pip install requests
or
pip install -r requirements.txt

See [requirements.txt]

## AI interactions (perplexity pro)






