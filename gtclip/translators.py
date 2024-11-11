from __future__ import annotations

class Translator:
    def __init__(self, target_lang: str) -> None:
        self._target_lang = target_lang
        pass
    def translate(self, text: str) -> str:
        return str(text)

class TranslatorGoogle(Translator):
    from google.cloud import translate_v2 as t
    _tclient = None
    def __new__(cls, target_lang: str) -> TranslatorGoogle:
        if cls._tclient is None:
            cls._tclient =  cls.t.Client()
            print("The translator client has been created.")
        return super().__new__(cls)
    def translate(self, text: str) -> str:
        result = self._tclient.translate(text, target_language=self._target_lang)
        return str(result["translatedText"])

class TranslatableStr(str):
    def __new__(cls, val: str, translator: Translator) -> TranslatableStr:
        self = super().__new__(cls, val)
        self._translator = translator
        return self
    def lang_translate(self) -> TranslatableStr:
        return TranslatableStr(self._translator.translate(self.__str__()), self._translator)
