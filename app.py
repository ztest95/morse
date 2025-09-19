

class MorseConverter:

    TEXT_TO_MORSE = {
        " ": "/", # Space between words
        "#": "#", # Placeholder for unknown characters
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "&": ".-...",
        "'": ".----.",
        "@": ".--.-.",
        ")": "-.--.-",
        "(": "-.--.",
        ":": "---...",
        ",": "--..--",
        "=": "-...-",
        "!": "-.-.--",
        ".": ".-.-.-",
        "-": "-....-",
        "×": "-..-",
        # "%": "----- -..-. -----",
        "+": ".-.-.",
        "\"": ".-..-.",
        "?": "..--..",
        "/": "-..-."
    }

    MORSE_TO_TEXT = {morse: char for char, morse in TEXT_TO_MORSE.items()}

    def text_to_morse(self, text):
        return " ".join(self.TEXT_TO_MORSE.get(ch.upper(), "#") for ch in text.strip())

    def morse_to_text(self, code):
        return "".join(self.MORSE_TO_TEXT.get(symbol, "#") for symbol in code.strip().split())