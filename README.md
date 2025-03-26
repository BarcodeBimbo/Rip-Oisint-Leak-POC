<div align="center">
  <img src="https://github.com/user-attachments/assets/87a9f173-987a-4f75-bb06-362a5a0fc4a2" alt="RipOsintLeak" height="200">
</div>

<p align="center">
  <a href="https://discord.gg/xboxmods">
    <img src="https://discord.com/api/guilds/319560327719026709/widget.png?style=shield" alt="Discord Server">
  </a>
  <a href="https://www.python.org/downloads/">
    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/Red-Discordbot">
  </a>
</p>

# OSINTLeak Username Search Tool

## Description
This Python script allows you to search for username information using the OSINTLeak API. It provides a simple command-line interface to search for usernames and decrypt the retrieved data.

## The Start

Created an account found the search api endpoint via dev-tools
<div align="center">
  <img src="https://github.com/user-attachments/assets/bdd3b2f1-8bfa-40ee-b5ba-124bd373fc67" alt="RipOsintLeak">
</div>

After creating a request to the api i found that the response was encoded, so i need to dig abit to learn how data was being served on the frontend

## More Digging

Then I started reversing the js
```python
import requests, jsbeautifier

def js_beautifier(url):
    response  = requests.get(url=url)
    if response.ok:
        return jsbeautifier.beautify(response.text)
 
with open("swag.js", "w", encoding="utf-8") as clean_js:
    clean_js.write(js_beautifier("https://osintleak.com/_nuxt/D-7P-sjM.js"))
```

On line: 2868 is the start of the decoder logic.

<div align="center">
  <img src="https://github.com/user-attachments/assets/adf07b06-d4fc-4d25-96ce-6052dfa67dd7" alt="RipOsintLeak" >
</div>

Now that i have the logic on how data is served to the frontend it was time to recrate this in python

---

## Features
- Search for usernames on OSINTLeak
- Decrypt and save search results
- Copy decrypted results to clipboard
- Save results to a local JSON file

## Prerequisites
- Python 3.7+
- Required libraries:
  - requests
  - pyperclip
  - json
  - base64

## Installation

1. Clone the repository:
```bash
git clone https://github.com/BarcodeBimbo/Rip-Oisint-Leak-POC.git
cd Rip-Oisint-Leak-POC
```

2. Install required dependencies:
```bash
pip install requests pyperclip
```

## Configuration
1. Open `riposintleak.py`
2. Replace the empty `token = ""` with your OSINTLeak authentication token without the Bearer

## Usage
```bash
python riposintleak.py
```
When prompted, enter the username you want to search.

## Notes
- Requires a valid OSINTLeak authentication token
- Decrypted results are saved to `decrypted_output.json`
- Results are also copied to clipboard

## License
This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

## 🧑‍💻 Developer

- **Name:** Joshua 
- **Contact:** @BarcodeBimbo
- **Version:** 1.0.0
- **Updated:** March 22, 2025

## ⚠️ Disclaimer

This is a reverse-engineered, unofficial API tool intended for educational purposes. Use responsibly and ethically.


