import os

from PyPDF2 import PdfFileReader
import requests

filename = 'poem'
with open(f'pdfs/{filename}.pdf', 'rb') as file:
    pdf = PdfFileReader(file)
    text = pdf.getPage(0).extractText()
    print()

params = {
    'key': os.getenv('VOICE'),
    'src': text,
    'hl': 'en-us',
    'c': 'MP3',
}

response = requests.get('https://api.voicerss.org', params=params)
with open(f'tts/{filename}.mp3', 'wb') as file:
    file.write(response.content)
