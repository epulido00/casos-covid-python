## Proyecto en Flask 

Para empezar el proyecto se hizo en flask, para instalar y que te funcione todo correctamente ocupas correr:

`pip install requests`

`pip install feedparser`

son 2 de las librerias que use para consumir API's y RSS


## Pasos que seguí

1.- Inicié mi proyecto con flask y en el archivo app.py hice todo el código

2.- Cree mi función covid() en la ruta "/" para que sea nuestro index

```

@app.route('/')
def covid():
	#Aqui va el código

```

3.- Hice mi request del link [https://api.covid19api.com/summary](https://api.covid19api.com/summary)

```
casos = requests.get('https://api.covid19api.com/summary')
```

4.- Convertí mi response json en una lista de python y luego guarde los casos que me importaban en diferentes variables

```
casos = casos.json()

casos_mundiales = casos['Global']
casos_pais = casos['Countries']
```
---
#### **Estos son pasos extra que le agregué**

E1.- Hice una request de un RSS para consumir noticias y guarde en una variable
```
noticias = feedparser.parse("https://www.who.int/feeds/entity/csr/don/es/rss.xml")
noticias = noticias.entries
```
---
5.- Se crea la vista haciendo el render de un archivo HTML y mandamos nuestras variables

```
return render_template("covid19.html", casos_mundiales=casos_mundiales, casos_pais=casos_pais, noticias=noticias)
```

Nuestro función completa quedaría de esta manera:

```
@app.route('/')
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
```

Ya por último utilizamos nuestros datos en la vista HTML [covid19.html](https://github.com/epulido00/casos-covid-python/blob/main/templates/covid19.html) que está dentro del repositorio.

