import requests
from bs4 import BeautifulSoup

def fetch_and_analyze(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Fetching the title of the page
            title = soup.find('title').text if soup.find('title') else 'No Title'
            
            # Analyzing images
            images = soup.find_all('img')
            total_images = len(images)
            images_with_alt = sum(1 for img in images if img.get('alt'))
            images_without_alt = total_images - images_with_alt
            
            # Fetching meta description and keywords
            description = soup.find('meta', attrs={'name': 'description'})
            description = description['content'] if description else 'No Description'
            keywords = soup.find('meta', attrs={'name': 'keywords'})
            keywords = keywords['content'].split(',') if keywords else []
            
            return {
                "title": title,
                "total_images": total_images,
                "images_with_alt": images_with_alt,
                "images_without_alt": images_without_alt,
                "meta": {
                    "description": description,
                    "keywords": keywords
                }
            }
    except requests.RequestException as e:
        return {"error": str(e)}
