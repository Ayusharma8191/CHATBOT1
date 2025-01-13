import requests
from bs4 import BeautifulSoup 


# Function to scrape website content
def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract specific content (e.g., paragraphs)
        content = ' '.join([p.text for p in soup.find_all('p')])
        return content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return "" 
    
    