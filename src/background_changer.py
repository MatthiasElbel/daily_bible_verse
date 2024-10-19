import os
import subprocess


class BackgroundChanger:
    @staticmethod
    def change_background(image_path):
        """Ändert das Desktop-Hintergrundbild auf das angegebene Bild."""
        if not os.path.isfile(image_path):
            print(f"Bild nicht gefunden: {image_path}")
            return

        image_uri = f"file://{os.path.abspath(image_path)}"

        try:
            subprocess.run(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", image_uri], check=True)
            subprocess.run(["gsettings", "set", "org.gnome.desktop.background", "picture-uri-dark", image_uri],
                           check=True)
            print(f"Hintergrundbild erfolgreich geändert: {image_path}")
        except subprocess.CalledProcessError as e:
            print(f"Fehler beim Ändern des Hintergrundbilds: {e}")
