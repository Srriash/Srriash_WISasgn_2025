# pubmed_api.py
import requests
import csv
import os

BASE_ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
BASE_ESUMMARY = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

def fetch_pubmed_ids(query, retmax=20):
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": retmax,
        "sort": "pub+date"   # <-- Fetch by recency!
    }
    resp = requests.get(BASE_ESEARCH, params=params)
    resp.raise_for_status()
    ids = resp.json()["esearchresult"].get("idlist", [])
    return ids

def fetch_article_metadata(pmid_list):
    if not pmid_list:
        return []
    params = {
        "db": "pubmed",
        "id": ",".join(pmid_list),
        "retmode": "json"
    }
    resp = requests.get(BASE_ESUMMARY, params=params)
    resp.raise_for_status()
    summaries = resp.json()["result"]
    uids = summaries.pop("uids", None)
    return [summaries[pmid] for pmid in summaries if isinstance(summaries[pmid], dict)]

def save_metadata_to_csv(items, filename):
    if not items:
        raise ValueError("No data to save.")
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    keys = ["uid", "title", "authors", "pubdate", "source"]
    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(keys)
        for it in items:
            authors = "; ".join([a['name'] for a in it.get("authors", [])])
            row = [it.get('uid', ''),
                   it.get('title', ''),
                   authors,
                   it.get('pubdate', ''),
                   it.get('source', '')]
            writer.writerow(row)
