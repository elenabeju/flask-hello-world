from flask import Flask
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def home():
    res = requests.get('https://www.kinopoisk.cx/film/777/')



    return res.text

@app.route('/about')
def about():
    return 'About'
