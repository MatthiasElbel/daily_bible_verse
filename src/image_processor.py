import os
from PIL import Image, ImageDraw, ImageFont


class ImageProcessor:
    @staticmethod
    def create_image_with_text(image_path, wrapped_lines, output_path):
        """Fügt Text zu einem Bild hinzu und speichert das Bild."""
        image = Image.open(image_path)

        try:
            font_size = 50
            font = ImageFont.truetype("ressources/Bigrode.otf", font_size)
        except IOError:
            print("Schriftart nicht gefunden, Standard verwendet.")
            font = ImageFont.load_default()

        draw = ImageDraw.Draw(image)
        text_position = (80, 160)
        text_color = (255, 255, 255)
        y_offset = text_position[1]

        for w in wrapped_lines:
            for line in w:
                bbox = draw.textbbox((text_position[0], y_offset), line, font=font)
                line_height = bbox[3] - bbox[1]
                draw.text((text_position[0], y_offset), line, fill=text_color, font=font)
                y_offset += line_height + 10
            y_offset += 60

        image.save(output_path)
        print(f"Bild wurde aktualisiert und als '{output_path}' gespeichert.")
        return output_path
