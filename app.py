import sqlite3
from flask import Flask
from flask import render_template
import requests
import feedparser

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/covid19')
def covid():

	#Consumir casos covid
	casos = requests.get('https://api.covid19api.com/summary')

	casos = casos.json()

	casos_mundiales = casos['Global']
	casos_pais = casos['Countries']

	#Noticias RSS de la OMS
	noticias = feedparser.parse("https://www.who.int/feeds/entity/csr/don/es/rss.xml")
	noticias = noticias.entries

	return render_template("covid19.html", casos_mundiales=casos_mundiales, casos_pais=casos_pais, noticias=noticias)

if __name__ == '__main__':
    app.run()