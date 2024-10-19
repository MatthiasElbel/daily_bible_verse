
from datetime import datetime
from text_handler import TextHandler
from src.image_fetcher import ImageFetcher
from web_scraper import WebScraper
from src.image_processor import ImageProcessor
from src.background_changer import BackgroundChanger

if __name__ == '__main__':
    image_folder = "/home/matthi/VersDesTages/backgrounds/" # Folder with possible Background Images
    url = "https://www.joyce-meyer.de/fuer-dich/taegliche-andacht-von-joyce-meyer/" # Url from the texts

    css_selectors = [
        ".andacht-datum",
        ".elementor-element-e2e805a > div:nth-child(1) > div:nth-child(1) > blockquote:nth-child(1) > p:nth-child(2)",
        ".elementor-element-e2e805a > div:nth-child(1) > div:nth-child(1) > blockquote:nth-child(1) > cite:nth-child(3) > span:nth-child(1)",
        ".elementor-element-e56ca4f > div:nth-child(1) > h2:nth-child(1)",
        ".elementor-element-cea7568 > div:nth-child(1)"
    ]
    texts = WebScraper.fetch_text_from_web(url, css_selectors)
    max_words_per_row = 100
    wrapped_lines = [TextHandler.wrap_text_by_words(text, max_words_per_row) for text in texts]

    image_path = ImageFetcher.get_random_image_from_folder(image_folder)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_image_path = f"/home/matthi/VersDesTages/output_{timestamp}.png"

    ImageProcessor.create_image_with_text(image_path, wrapped_lines, output_image_path)
    BackgroundChanger.change_background(output_image_path)
