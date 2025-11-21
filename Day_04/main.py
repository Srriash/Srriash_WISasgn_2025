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

    # Ask for user-selected destination as before
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
    filename = f"pubmed_{safe_q}_{timestamp}.csv"

    # Save to user-selected location
    user_path = os.path.join(dest_folder, filename)
    save_metadata_to_csv(articles, user_path)
    print(f"Saved metadata for {len(articles)} articles to: {user_path}")

    # --- NEW: save also to repo data/ folder (relative to where main.py is run) ---
    repo_data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
    os.makedirs(repo_data_dir, exist_ok=True)
    repo_path = os.path.join(repo_data_dir, filename)
    save_metadata_to_csv(articles, repo_path)
    print(f"Also saved metadata to repository folder: {repo_path}")

if __name__ == "__main__":
    main()
