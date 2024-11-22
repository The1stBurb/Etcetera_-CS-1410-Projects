import requests
from bs4 import BeautifulSoup
import csv
import time

def scrape_website(base_url, num_pages):
    all_data = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    for page_num in range(1, num_pages + 1):
        url = f"{base_url}{page_num}"
        print(f"Scraping page {page_num}...")

        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')

            # Example: Extract titles and links
            articles = soup.find_all('article')
            for article in articles:
                title = article.find('h2').text.strip() if article.find('h2') else 'No Title'
                link = article.find('a')['href'] if article.find('a') else 'No Link'
                all_data.append({'title': title, 'link': link})

            time.sleep(2)  # Be polite, wait between requests

        except requests.RequestException as e:
            print(f"Error scraping {url}: {e}")

    return all_data

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'link'])
        writer.writeheader()
        for item in data:
            writer.writerow(item)

def main():
    base_url = "https://example.com/page/"  # Replace with the actual URL
    num_pages = 5  # Number of pages to scrape

    scraped_data = scrape_website(base_url, num_pages)
    save_to_csv(scraped_data, 'scraped_data.csv')
    print(f"Scraped {len(scraped_data)} items and saved to scraped_data.csv")

if __name__ == "__main__":
    main()