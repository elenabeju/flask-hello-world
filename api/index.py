from flask import Flask
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def home():
    res = requests.get('https://www.kinopoisk.cx/film/777/')


    soup = BeautifulSoup(res.text, 'html.parser')


    script_tag = soup.find('script', language='javascript')
    script_content = script_tag.string
    start_index = script_content.find("document.location.href='") + len("document.location.href='")
    end_index = script_content.find("'", start_index)
    redirect_url = script_content[start_index:end_index]

    return redirect_url

@app.route('/about')
def about():
    return 'About'
