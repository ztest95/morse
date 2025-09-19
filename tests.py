import unittest

from app import MorseConverter


class TestMorseConverter(unittest.TestCase):

    def setUp(self):
        self.converter = MorseConverter()

    def test_single_letters(self):
        self.assertEqual(self.converter.text_to_morse("A"), ".-")
        self.assertEqual(self.converter.text_to_morse("B"), "-...")
        self.assertEqual(self.converter.text_to_morse("Z"), "--..")

    def test_full_words(self):
        self.assertEqual(self.converter.text_to_morse("SOS"), "... --- ...")
        self.assertEqual(self.converter.text_to_morse("HELLO"), ".... . .-.. .-.. ---")

    def test_sentence_with_space(self):q
        self.assertEqual(
            self.converter.text_to_morse("HELLO WORLD"),
            ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
        )

    def test_mixed_case_input(self):
        self.assertEqual(self.converter.text_to_morse("Hello"), ".... . .-.. .-.. ---")

    def test_numbers(self):
        self.assertEqual(self.converter.text_to_morse("123"), ".---- ..--- ...--")

    def test_punctuation(self):
        self.assertEqual(self.converter.text_to_morse("?"), "..--..")
        self.assertEqual(self.converter.text_to_morse("!"), "-.-.--")

    def test_empty_string_to_morse(self):
        self.assertEqual(self.converter.text_to_morse(""), "")

    def test_extra_spaces_in_text(self):
        self.assertEqual(self.converter.text_to_morse("         "), "")
        self.assertEqual(self.converter.text_to_morse("   O   "), "---")

    def test_unknown_character_to_morse(self):
        self.assertEqual(self.converter.text_to_morse("~"), "#")
        self.assertEqual(self.converter.text_to_morse("*"), "#")
        self.assertEqual(self.converter.text_to_morse("^"), "#")

    def test_single_morse_letters(self):
        self.assertEqual(self.converter.morse_to_text(".-"), "A")
        self.assertEqual(self.converter.morse_to_text("-..."), "B")

    def test_full_word_from_morse(self):
        self.assertEqual(self.converter.morse_to_text(".... . .-.. .-.. ---"), "HELLO")

    def test_sentence_from_morse(self):
        self.assertEqual(
            self.converter.morse_to_text(".... . .-.. .-.. --- / .-- --- .-. .-.. -.."),
            "HELLO WORLD"
        )

    def test_numbers_from_morse(self):
        self.assertEqual(self.converter.morse_to_text(".---- ..--- ...--"), "123")

    def test_punctuation_from_morse(self):
        self.assertEqual(self.converter.morse_to_text("..--.."), "?")
        self.assertEqual(self.converter.morse_to_text("-.-.--"), "!")

    def test_empty_morse_to_text(self):
        self.assertEqual(self.converter.morse_to_text(""), "")

    def test_invalid_morse_symbol(self):
        self.assertEqual(self.converter.morse_to_text("... --- ... .-.-.-.-.-"), "SOS#")

    def test_extra_spaces_in_morse(self):
        self.assertEqual(self.converter.morse_to_text("....   ."), "HE")

    def test_round_trip_text_to_morse_to_text(self):
        text = "PYTHON 3"
        morse = self.converter.text_to_morse(text)
        result = self.converter.morse_to_text(morse)
        self.assertEqual(result, text.upper())

    def test_round_trip_morse_to_text_to_morse(self):
        morse = "... --- ..."
        text = self.converter.morse_to_text(morse)
        result = self.converter.text_to_morse(text)
        self.assertEqual(result, morse)

    def test_extended_symbols_to_morse(self):
        self.assertEqual(self.converter.text_to_morse("&"), ".-...")
        self.assertEqual(self.converter.text_to_morse("'"), ".----.")
        self.assertEqual(self.converter.text_to_morse("@"), ".--.-.")
        self.assertEqual(self.converter.text_to_morse("("), "-.--.")
        self.assertEqual(self.converter.text_to_morse(")"), "-.--.-")
        self.assertEqual(self.converter.text_to_morse(":"), "---...")
        self.assertEqual(self.converter.text_to_morse(","), "--..--")
        self.assertEqual(self.converter.text_to_morse("="), "-...-")
        self.assertEqual(self.converter.text_to_morse("!"), "-.-.--")
        self.assertEqual(self.converter.text_to_morse("."), ".-.-.-")
        self.assertEqual(self.converter.text_to_morse("-"), "-....-")
        self.assertEqual(self.converter.text_to_morse("×"), "-..-")
        self.assertEqual(self.converter.text_to_morse("0/0"), "----- -..-. -----")
        self.assertEqual(self.converter.text_to_morse("+"), ".-.-.")
        self.assertEqual(self.converter.text_to_morse("\""), ".-..-.")
        self.assertEqual(self.converter.text_to_morse("?"), "..--..")
        self.assertEqual(self.converter.text_to_morse("/"), "-..-.")

    def test_extended_symbols_from_morse(self):
        self.assertEqual(self.converter.morse_to_text(".-..."), "&")
        self.assertEqual(self.converter.morse_to_text(".----."), "'")
        self.assertEqual(self.converter.morse_to_text(".--.-."), "@")
        self.assertEqual(self.converter.morse_to_text("-.--."), "(")
        self.assertEqual(self.converter.morse_to_text("-.--.-"), ")")
        self.assertEqual(self.converter.morse_to_text("---..."), ":")
        self.assertEqual(self.converter.morse_to_text("--..--"), ",")
        self.assertEqual(self.converter.morse_to_text("-...-"), "=")
        self.assertEqual(self.converter.morse_to_text("-.-.--"), "!")
        self.assertEqual(self.converter.morse_to_text(".-.-.-"), ".")
        self.assertEqual(self.converter.morse_to_text("-....-"), "-")
        self.assertEqual(self.converter.morse_to_text("-..-"), "×")
        self.assertEqual(self.converter.morse_to_text("----- -..-. -----"), "0/0")
        self.assertEqual(self.converter.morse_to_text(".-.-."), "+")
        self.assertEqual(self.converter.morse_to_text(".-..-."), "\"")
        self.assertEqual(self.converter.morse_to_text("..--.."), "?")
        self.assertEqual(self.converter.morse_to_text("-..-."), "/")

if __name__ == "__main__":
    unittest.main()
