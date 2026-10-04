import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_book_data(num_pages=5):
    """Scrape book data (title, price, rating, availability) from books.toscrape.com
    across the specified number of pages, and return it as a DataFrame."""
    
    all_books = []
    
    for page_num in range(1, num_pages + 1):
        page_url = f"https://books.toscrape.com/catalogue/page-{page_num}.html"
        response = requests.get(page_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        books = soup.find_all('article', class_='product_pod')
        
        for book in books:
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text
            rating = book.find('p', class_='star-rating')['class'][1]
            availability = book.find('p', class_='instock availability').text.strip()
            
            all_books.append({
                'title': title,
                'price': price,
                'rating': rating,
                'availability': availability
            })
    
    df = pd.DataFrame(all_books)
    return df

# Quick test when running this file directly
if __name__ == "__main__":
    df = extract_book_data()
    print(df.shape)
    print(df.head())