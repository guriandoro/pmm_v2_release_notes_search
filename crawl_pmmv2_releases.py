import requests
from bs4 import BeautifulSoup
import re
import sys

def crawl_and_search(base_url, keyword):
    # Define the regex pattern for version 2.x pages
    pattern = re.compile(r'2\.\d+')

    # Function to get all links from a page
    def get_links(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True) if pattern.search(a['href'])]
        return links

    # Function to search for the keyword in the main HTML text
    def search_keyword(url, keyword):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract the main content text from the div with class "md-content"
        main_content = soup.find('div', class_='md-content')
        if main_content:
            page_text = main_content.get_text()
            if keyword.lower() in page_text.lower():
                print(f"=> Keyword found on page: {url}\n")
        else:
            print(f"No main content found on page: {url}")

    # Start crawling from the base URL
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    initial_links = get_links(base_url)
    if not initial_links:
        print("No links found on the base URL.")
        return

    crawled_urls = set()
    for link in initial_links:
        link = 'https://docs.percona.com/percona-monitoring-and-management/release-notes/' + link  # Construct the full URL
        if link not in crawled_urls:
            print(f"Crawling page: {link}", file=sys.stderr)
            search_keyword(link, keyword)
            crawled_urls.add(link)
#        else:
#            print(f"Skipping already crawled URL: {link}")

if __name__ == "__main__":
    base_url = "https://docs.percona.com/percona-monitoring-and-management/release-notes/index.html"
    if len(sys.argv) > 1:
        # Join all arguments to form the keyword string
        keyword = ' '.join(sys.argv[1:])
    else:
        keyword = input("Enter the keyword(s) to search for: ")
    crawl_and_search(base_url, keyword)
