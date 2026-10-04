# Web Scraping & Data Warehouse Pipeline

## Overview
This project builds a modular ETL pipeline that scrapes book data directly from HTML (not an API), cleans it, and loads it into a local SQLite database. It's the fifth project in a broader Data Engineering portfolio, introducing web scraping with BeautifulSoup and handling pagination across multiple pages — while reusing the same modular extract/transform/load structure from previous projects.

## Data Source
- **Website:** [Books to Scrape](https://books.toscrape.com/) — a sandbox site purpose-built for scraping practice, with no restrictions on crawling (confirmed via its open structure and public documentation)
- **Scope:** 5 pages scraped (100 books total, out of 1,000 available across 50 pages)

## Pipeline Structure
Same modular ETL pattern as previous projects:

- **`step1_extract.py`** — scrapes book title, price, rating, and availability from multiple pages using `requests` and `BeautifulSoup`
- **`step2_transform.py`** — cleans a character encoding issue in the price field, converts price to a proper numeric type, and converts star rating from word form (e.g., "Three") to a number
- **`step3_load.py`** — loads the cleaned data into a SQLite database (using a full replace, since this is a one-time scrape snapshot rather than accumulating data over time)
- **`main.py`** — orchestrates the full pipeline in sequence

## What Was Done
- Investigated the target website's HTML structure to identify where book data lives (`<article class="product_pod">` elements)
- Extracted title, price, star rating, and stock availability for each book
- Implemented pagination to loop through multiple pages automatically rather than scraping just one page
- Identified and fixed a character encoding issue in scraped prices (a stray `Â` character preceding the £ symbol)
- Converted star ratings from descriptive text (e.g., "Three") into numeric values using a mapping dictionary
- Loaded 100 cleaned book records into a `books` table in a local SQLite database

## Project Structure
```
de-05-web-scraping-warehouse/
├── data/
│ └── books_warehouse.db # SQLite database with cleaned book data (not tracked in Git)
├── notebooks/
│ └── exploration.ipynb # Initial HTML structure investigation and extraction testing
├── src/
│ ├── step1_extract.py # Extract: scrape book data across multiple pages
│ ├── step2_transform.py # Transform: clean price and rating fields
│ ├── step3_load.py # Load: write cleaned data into SQLite
│ └── main.py # Orchestrates the full pipeline
├── requirements.txt
└── README.md
```

## Tech Stack
- Python
- Requests
- BeautifulSoup (bs4)
- Pandas
- SQLite

## Key Takeaways
This project introduced web scraping as a data extraction method distinct from APIs — requiring direct HTML parsing rather than working with structured JSON. It also introduced pagination handling (looping through multiple pages to build a larger dataset) and reinforced the importance of validating scraped data closely, since web scraping is more prone to subtle formatting issues (like the character encoding problem encountered here) than working with clean API responses.

## How to Run
1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the full pipeline: `python src/main.py`
4. Open `data/books_warehouse.db` in DB Browser for SQLite to view the loaded data