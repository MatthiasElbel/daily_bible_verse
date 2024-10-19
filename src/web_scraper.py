import requests
from bs4 import BeautifulSoup


class WebScraper:
    @staticmethod
    def fetch_text_from_web(url, css_selectors):
        """Holt den Text von der angegebenen URL und gibt ihn als Liste von Absätzen zurück.

        css_selectors: Liste von CSS-Selektoren
        """
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Fehler beim Abrufen der URL: {response.status_code}")
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        texts = []

        # Durchlaufe alle CSS-Selektoren
        for css_selector in css_selectors:
            elements = soup.select(css_selector)
            for element in elements:
                text = element.get_text(separator=" ").strip()
                if text:
                    texts.append(text)

        return texts
