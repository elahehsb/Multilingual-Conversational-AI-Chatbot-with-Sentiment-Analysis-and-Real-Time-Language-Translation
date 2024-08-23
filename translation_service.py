from googletrans import Translator

class TranslatorService:
    def __init__(self):
        self.translator = Translator()

    def translate(self, text, dest_language):
        translation = self.translator.translate(text, dest=dest_language)
        return translation.text

if __name__ == "__main__":
    translator = TranslatorService()
    translated_text = translator.translate("Hello, how are you?", "es")
    print("Translated Text:", translated_text)
