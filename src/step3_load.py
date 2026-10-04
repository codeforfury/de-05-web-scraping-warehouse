import sqlite3
import pandas as pd

def load_to_database(df, db_path='data/books_warehouse.db', table_name='books'):
    """Load the cleaned book data into a SQLite database table, replacing any existing data."""
    
    # Connect to (or create) the database file
    conn = sqlite3.connect(db_path)
    
    # Using 'replace' here since this is a one-time scrape snapshot, not accumulating data over time
    # (different from Project 4's weather pipeline, which used 'append' to build history)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    
    conn.close()
    print(f"Loaded {len(df)} rows into '{table_name}' table in {db_path}")

# Quick test when running this file directly
if __name__ == "__main__":
    from step1_extract import extract_book_data
    from step2_transform import transform_book_data
    
    raw_df = extract_book_data()
    cleaned_df = transform_book_data(raw_df)
    load_to_database(cleaned_df)