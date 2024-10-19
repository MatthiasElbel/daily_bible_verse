class TextHandler:
    @staticmethod
    def wrap_text_by_words(text, max_length):
        """Teilt den Text in mehrere Zeilen um, basierend auf einer maximalen Anzahl von Zeichen, ohne Wörter zu trennen."""
        words = text.split()
        lines = []
        current_line = ""

        for word in words:
            if len(current_line) + len(word) + 1 <= max_length:
                if current_line:
                    current_line += " "
                current_line += word
            else:
                lines.append(current_line)
                current_line = word

        if current_line:
            lines.append(current_line)

        return lines
