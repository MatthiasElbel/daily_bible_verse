import os
import random


class ImageFetcher:
    @staticmethod
    def get_random_image_from_folder(folder_path):
        """Wählt ein zufälliges .jpg-Bild aus einem Ordner aus."""
        images = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]
        if not images:
            raise FileNotFoundError("Keine .jpg-Bilder im angegebenen Ordner gefunden.")
        return os.path.join(folder_path, random.choice(images))
