# Projekt Hollymovies

## Sylabus
### 5. Bře 2025, St 17:30–21:00
- Prošli jsme slidy 1-15
- Úvod
- Vytvoření projektu
- Vytvoření aplikace
- Návrh funkcionality
- Návrh databáze

### 6. Bře 2025, Čt 17:30–20:30
- Prošli jsme slidy 16-32
- ORM - modely (Genre, Country, Creator, Movie)
- migrace
- admin panel
- shell
- fixtures

### 10. Bře 2025, Po 17:30–21:00
- Dotazy (Queries)
- Šablony (templates)
- Class-Based Views (CBV)
- Seznam filmů (feature 1)
- Seznam tvůrců (feature 4)
- Detail filmu (feature 2)

### 11. Bře 2025, Út 17:30–20:30
### 12. Bře 2025, St 17:30–21:00
### 13. Bře 2025, Čt 17:30–20:30
### 24. Bře 2025, Po 17:30–20:30
### 25. Bře 2025, Út 17:30–20:30
### 26. Bře 2025, St 17:30–20:30
### 27. Bře 2025, Čt 17:30–20:30
### 31. Bře 2025, Po 17:30–20:30
### 1. Dub 2025, Út 17:30–21:00
### 3. Dub 2025, Čt 17:30–21:30

## Popis projektu 
- [x] 1 zobrazit seznam filmů
- [x] 2 zobrazit detaily filmu
- [ ] 3 práce s filmem v databázi
  - [ ] přidání nového filmu
  - [ ] editace filmu
  - [ ] mazání filmu 
- [x] 4 zobrazit seznam herců a režisérů
- [ ] 5 zobrazit detail (biografie) herce/režiséra
- [ ] 6 práce s tvůrcem v databázi
  - [ ] přidání nového tvůrce
  - [ ] editace tvůrce
  - [ ] mazání tvůrce  
- [ ] 7 filtrování filmů
  - [ ] 1 podle žánru
  - [ ] 2 podle země
  - [ ] 3 podle režiséra
  - [ ] 4 podle herce
  - [ ] 5 podle roku
- [ ] 8 hledání 
  - [ ] 1 filmů
  - [ ] 2 herců/režisérů
- [ ] 9 hodnocení filmů
- [ ] 10 watchlist 
- [ ] 11 přidávání ocenění
- [ ] 12 zobrazení seznamu seriálů
- [ ] 13 zobrazení detailu seriálu/epizody


## Django
### Instalace
```bash
pip install django
```
```bash
pip freeze > requirements.txt
```

### Struktura projektu
- `holymovies` - složka projektu (obsahuje informace o celém projektu)
  - `__init__.py` - je zde jen proto, aby daná složka byla package
  - `asgi.py` - nebudeme potřebovat
  - `settings.py` - nastavení projektu
  - `urls.py` - zde jsou nastavené url cesty
  - `wsgi.py` - nebudeme potřebovat
- `manage.py` - hlavní skript pro práci s projektem (spouštění serveru, testů, migrací,...)

### Spuštění serveru
```bash
python manage.py runserver
```

Případně můžeme zadat ručně číslo portu:
```bash
python manage.py runserver 8001
```

### Aplikace
#### Vytvoření aplikace
```bash
python manage.py startapp <nazev_aplikace>
```

> [!WARNING]
> Nesmíme zapomenou zaregistrovat aplikaci do souboru `settings.py`:
> ```python
> INSTALLED_APPS = [
>     'django.contrib.admin',
>     'django.contrib.auth',
>     'django.contrib.contenttypes',
>     'django.contrib.sessions',
>     'django.contrib.messages',
>     'django.contrib.staticfiles',
>     
>     'viewer',
> ]
> ```

#### Struktura aplikace
- `viewer` - složka aplikace
  - `migrations` - složka obsahující migrační skripty 
  - `__init__.py` - slouží jen k tomu, aby složka byla package
  - `admin.py` - zde budeme registrovat modely, které budeme chtít zobrazit v admin sekci
  - `apps.py` - nastavení aplikace
  - `models.py` - definice modelů (schéma databáze)
  - `tests.py` - testy
  - `views.py` - funkcionalita
  
## Databáze
- [x] Genre
  - [x] name (String) 

- [x] Country
  - [x] name (String) 
  - [x] flag (Image?) 

- [x] Creator
  - [x] name (String)
  - [x] surname (String)
  - [x] country (-> Country)
  - [x] date_of_birth (Date)
  - [x] date_of_death (Date)
  - [x] biography (String) 
  - [ ] awards (n:m -> ??)
  - [x] acting (n:m -> Movie)
  - [x] directing (n:m -> Movie) 

- [x] Movie
  - [x] title_orig (String)
  - [x] title_cz (String)
  - [x] genres (n:m -> Genre)
  - [x] countries (n:m -> Country)
  - [x] length (Integer)
  - [x] actors (n:m -> Creator)
  - [x] directors (n:m -> Creator)
  - [x] description (String)
  - [x] released_date (Date)
  - [ ] rating (Float)
  - [ ] images (1:n -> ??)
  - [ ] video_url (String)

- [ ] Review
  - [ ] reviewer (-> User) 
  - [ ] movie (-> Movie)
  - [ ] rating (Integer, 1-5 hvězdiček)
  - [ ] comment (String) 
  - [ ] created (DateTime)
  - [ ] updated (DateTime) 

- [ ] User (defaultní z Django)

### Migrace 
Migrace mění schéma databáze a skládá se ze dvou kroků:
- `python manage.py makemigrations` - vytvoří migrační skript popisující změny
- `python manage.py migrate` - spustí migrační skripty -> změnu schématu databáze
 
### Administrační panel
Musíme nejprve vytvořit superuser: `python manage.py createsuperuser`

Do souboru `viewer.admin.py` zaregistrujeme vytvořený model:
```python
from viewer.models import Genre
admin.site.register(Genre)
```

### DUMP/LOAD databáze
```bash
pip install django-dump-load-utf8
```

Přidáme `'django_dump_load_utf8',` do seznamu nainstalovaných aplikací 
`INSTALLED_APPS` v souboru `setting.py`.

#### DUMP
```bash
python manage.py dumpdatautf8 viewer --output .\files\fixtures.json 
```

#### LOAD
```bash
python manage.py loaddatautf8 .\files\fixtures.json 
```

### Dotazy (Queries)
#### .all()
Vrací kolekci všech nalezených záznamů z tabulky:
`Movie.objects.all()`

#### .get()
Vrátí jeden nalezený záznam (první, který splňuje podmínky):
`Movie.objects.get(id=1)`

#### .filter()
Vrací kolekci záznamů, které splňují podmínky:
`Movie.objects.filter(id=1)`

`Movie.objects.filter(title_orig="The Green Mile")`

`Movie.objects.filter(released_date__year=1994)`

`Movie.objects.filter(released_date__year__gt=1994)` -- `__gt` => "větší než" (greater then)

`Movie.objects.filter(released_date__year__gte=1994)` -- `__gte` => "větší rovno" (greater then equal)

`Movie.objects.filter(released_date__year__lt=1994)` -- `__lt` => "menší než" (less then)

`Movie.objects.filter(released_date__year__lte=1994)` -- `__lte` => "menší rovno" (less then equal)

`drama = Genre.objects.get(name="Drama")`

`Movie.objects.filter(genres=drama)`

`Movie.objects.filter(genres=Genre.objects.get(name="Drama"))`

`Movie.objects.filter(genres__name="Drama")`

`Movie.objects.filter(title_orig__contains="Gump")`

`Movie.objects.filter(genres__name="Drama", released_date__year=1999)` -- více podmínek, defaultně AND

`Movie.objects.filter(genres__name="Drama").filter(released_date__year=1999)` -- metody lze řetězit za sebe

`Movie.objects.filter(title_orig__in=["Forrest Gump", "The Green Mile"])`

`Movie.objects.filter(released_date__year=1994)`

`Movie.objects.exclude(released_date__year=1994)`

Test, zda existuje alespoň jeden záznam s danou podmínkou:
`Movie.objects.filter(released_date__year=1994).exists()`

Počet záznamů s danou podmínkou:
`Movie.objects.filter(released_date__year=1994).count()`

Uspořádání výsledků `.order_by()`:
`Movie.objects.all()`

`Movie.objects.all().order_by("released_date")` -- uspořádání vzestupně

`Movie.objects.all().order_by("-released_date")` -- uspořádání sestupně

Agregační funkce:
`from django.db.models import Avg, Min, Max`

`Movie.objects.aggregate(Avg("length"))`

`Movie.objects.aggregate(Avg("length"), Min("length"), Max("length"))`

Group_by:
`from django.db.models import Count`

`Movie.objects.values("genres").annotate(count=Count("genres"))`

#### Vytváření (Create)
`Genre.objects.create(name='Dokumentární')`

```python
scifi = Genre(name="Sci-fi")
scifi.save()
```

#### Aktualizece (Update)
`Movie.objects.filter(released_date__year=1994).update(length=123)`

```python
movie = Movie.objects.get(title_orig="Forrest Gump")
movie.length = 222
movie.save()
```

#### Mazání (Delete)
`Genre.objects.get(name="Dokumentární").delete()`

# Rady pro finální projekt
- jeden člen týmu vytvoří projekt
  - nainstaluje Django:
  ```bash
  pip install django
  ```
  - vytvoří soubor `requirements.txt`:
  ```bash
  pip freeze > requirements.txt 
  ```
  - vytvoří Django projekt:
  ```bash
  django-admin startproject <nazev_projektu> . 
  ```
  - nainstaluje `python-dotenv`:
  ```bash
  pip install python-dotenv
  pip freeze > requirements.txt 
  ```
  - vytvoří soubor `.env` v kořenovém adresáři projektu, který bude obsahovat
citlivé informace (`SECRET_KEY`, přístupové údaje do databáze,...) 
a nebude součástí repozitáře
  - v `settings.py` nahradíme `SECRET_KEY` proměnnou z `.env` souboru
  - vytvoří git repozitář
    - vytvoří `.gitignore` soubor 
    ```git
    /.idea
    /.env
    /db.sqlite3
    ```
    - odešle repozitář na GitHub
    - nasdílí s ostatními členy týmu adresu repozitáře
    - nastaví spolupracovníky (Settings -> Colaborators -> Add people)
- ostatní členové
  - naklonují projekt
  - vytvoří virtuální prostředí (`.venv`)
  - nainstalují si potřebné balíčky ze souboru `requirements.txt`:
  ```bash
  pip install -r requirements.txt 
  ```
  - vytvoří si `.env` soubor obsahující `SECRET_KEY`
