# jdszr12-git_squad

## Zawartość
* [Ogólne](#ogolne)
* [Wykorzystane narzędzia](#wykorzystane-narzedzia)
* [Setup](#setup)

## Ogólne
Projekt oceniający popularność i atrakcyjność lotnisk w Indiach, w latach 2015 i 2016. Selekcja została dokonana w oparciu o tabele przedstawiającą połączenia z i do miast w Indiach. Plik `csv` zawierający nieobrobione dane znajduje się w serwisie kaggle.com pod adresem:
https://www.kaggle.com/datasets/rajanand/international-air-traffic-from-and-to-india

## Wykorzystane narzędzia
Prezentacja powstała w oparciu o narzędzia:
* Postgresql
* Tableau
* Microsoft Powerpoint
	
## Autorzy
* Krzemińska Anna
* Licau Jarosław
* Lipiszko Maciej
* Nowak Ula
* Tkaczyk Paulina
```
$ cd ../portfolio-project
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```
