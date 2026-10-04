import pandas as pd

def transform_book_data(df):
    """Clean the raw scraped book DataFrame: fix price encoding/type, convert rating to a number."""
    
    # Remove the encoding artifact (Â) and the £ symbol, then convert price to a float
    # str.replace handles both characters; errors='coerce' would catch any leftover bad values (none expected here)
    df['price'] = df['price'].str.replace('Â£', '', regex=False).astype(float)
    
    # Convert rating from word form ("One" through "Five") to an actual number
    # using a mapping dictionary - this is a new, reusable technique for word-to-number conversion
    rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
    df['rating'] = df['rating'].map(rating_map)
    
    return df

# Quick test when running this file directly
if __name__ == "__main__":
    from step1_extract import extract_book_data
    
    raw_df = extract_book_data()
    cleaned_df = transform_book_data(raw_df)
    
    print(cleaned_df.dtypes)
    print(cleaned_df.head())