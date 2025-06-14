import requests
from bs4 import BeautifulSoup

def scrape_with_bs4(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    article = soup.find("div", {"class": "mw-parser-output"})
    if not article:
        return "Could not find article content."

    paragraphs = article.find_all("p") # type: ignore
    content = "\n".join(p.get_text() for p in paragraphs if p.get_text().strip())

    return content