import requests
from bs4 import BeautifulSoup
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("search_engine.db")
c = conn.cursor()

# Create table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS pages 
             (id INTEGER PRIMARY KEY, url TEXT, title TEXT, content TEXT)''')

def crawl(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        title = soup.title.string if soup.title else url
        content = soup.get_text()
        
        # Store in database
        c.execute("INSERT INTO pages (url, title, content) VALUES (?, ?, ?)", (url, title, content))
        conn.commit()

        print(f"✔ Crawled: {url}")

    except Exception as e:
        print(f"❌ Failed: {url} - {e}")

# Add websites to crawl
websites = [
    "https://www.youtube.com",
    "https://www.wikipedia.org"
]

for site in websites:
    crawl(site)

conn.close()
