import pyperclip

from gtclip.myargs import MyArgs
from gtclip.translators import TranslatableStr
from gtclip.translators import TranslatorGoogle

class Feature:
    def __init__(self) -> None:
        self.args = MyArgs()
    def do(self) -> int:
        return 0

class Default(Feature):
    import sys
    def __init__(self) -> None:
        super().__init__()
    def do(self) -> int:
        print("To end the input, press CTRL+D (Linux, Mac) or CTRL+Z (Windows)")
        #text = ''.join(self.sys.stdin.readlines())
        #print(TranslatableStr(text, TranslatorGoogle(self.args.target_lang)).lang_translate())
        loop = True
        while loop:
            try:
                text = self.sys.stdin.readline()
                print(TranslatableStr(text, TranslatorGoogle(self.args.target_lang)).lang_translate())
            except KeyboardInterrupt:
                loop = False
        return 0

class Monitor(Feature):
    def __init__(self) -> None:
        super().__init__()
    def do(self) -> int:
        print("Monitoring your clipboard...")
        print("To end the input, press CTRL+C.")
        loop = True
        while loop:
            try:
                print(TranslatableStr(pyperclip.waitForNewPaste(), TranslatorGoogle(self.args.target_lang)).lang_translate())
            except KeyboardInterrupt:
                loop = False
        return 0

class Once(Feature):
    def __init__(self) -> None:
        super().__init__()
    def do(self) -> int:
        print(TranslatableStr(self.args.text, TranslatorGoogle(self.args.target_lang)).lang_translate())
        return 0

class Factory:
    def create(self) -> Feature:
        a = MyArgs()
        ret = None
        if a.mode is a.Mode.ONCE:
            ret = Once()
        elif a.mode is a.Mode.MONITOR:
            ret = Monitor()
        else:
            ret = Default()
        return ret
