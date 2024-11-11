# What's gtclip

This is a python CLI application that monitors the clipboard, translates added content, and prints it to stdout.

## Requirements

This app uses the Google Cloud Translation API (Base v2).

Make a contract with Google and download your credential file (.json).
Please write the path to the downloaded your json file in the environment variable GOOGLE_APPLICATION_CREDENTIALS.

## Clone and python settings (an example for Windows)

```batchfile
git clone https://github.com/hatomania/gtclip
cd gtclip
python -m venv .venv
.\.venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -r .\requirements.txt
```

## Usage

Monitors the clipboard

```batchfile
python -m gtclip --monitor
```

Use ```--target_lang``` to specify the translate language. The default is 'en' that means English. It will be translated into English.

```batchfile
python -m gtclip --monitor --target_lang ja
```

If --monitor is not specified, text is taken from stdin.

```batchfile
python -m gtclip
```

If you want to translate only once, specify the text with --text.

```batchfile
python -m gtclip --text "こんにちは、世界！"
```
