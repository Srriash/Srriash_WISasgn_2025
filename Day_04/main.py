# main.py
import os
from datetime import datetime
from pubmed_api import fetch_pubmed_ids, fetch_article_metadata, save_metadata_to_csv

def main():
    print("Enter your PubMed search term using AND/OR operators if desired.\n")
    query = input("Example: 'CRISPR AND E. coli'\nSearch term: ")
    try:
        n = int(input("How many articles to fetch? (default 10): ") or "10")
    except ValueError:
        n = 10

    print("\nFetching PubMed IDs...")
    ids = fetch_pubmed_ids(query, retmax=n)
    if not ids:
        print("No articles found for your query.")
        return

    print(f"Fetching metadata for {len(ids)} articles...")
    articles = fetch_article_metadata(ids)

    # Prompt for local folder
    print("\nWhere would you like to save the CSV file?")
    print("For example: '/home/yourname/Documents' or 'C:\\Users\\yourname\\Documents'")
    dest_folder = input("Enter full folder path (leave empty for ~/Downloads): ").strip()
    if not dest_folder:
        dest_folder = os.path.expanduser("~/Downloads")
    if not os.path.isdir(dest_folder):
        print(f"Directory does not exist: {dest_folder}")
        return

    safe_q = "".join(c if c.isalnum() else "_" for c in query)[:50]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    fname = os.path.join(dest_folder, f"pubmed_{safe_q}_{timestamp}.csv")
    save_metadata_to_csv(articles, fname)
    print(f"Saved metadata for {len(articles)} articles to: {fname}")

if __name__ == "__main__":
    main()