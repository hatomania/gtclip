from __future__ import annotations

import argparse
from enum import Enum

class MyArgs:
    class Mode(Enum):
        DEFAULT = 1,
        MONITOR = 2,
        ONCE = 3,
    mode: Mode
    target_lang: str
    text: str

    _instance = None
    def __new__(cls) -> MyArgs:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        parser = argparse.ArgumentParser(description="This is a app that monitors your clipboard, translates added content, and prints it to stdout. Please see for detail: https://github.com/hatomania/gtclip")
        parser.add_argument("-L", "--target_lang", help="The language to be translated. (default: en)", default="en", type=str)
        parser.add_argument("--text", help="Translate the text once and then exit the program.", default="", type=str)
        parser.add_argument("--monitor", help="Monitors what is added to the clipboard and outputs it to stdout.", default=False, action='store_true')
        args = parser.parse_args()

        self.mode = self.Mode.DEFAULT
        if bool(args.monitor) is True:
            self.mode = self.Mode.MONITOR
        self.target_lang = args.target_lang
        self.text = args.text
        if len(self.text) > 0:
            self.mode = self.Mode.ONCE

MyArgs() # create the singleton instance here
