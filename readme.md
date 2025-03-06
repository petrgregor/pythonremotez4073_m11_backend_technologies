# Projekt Hollymovies

## Popis projektu 
- [ ] 1 zobrazit seznam filmů
- [ ] 2 zobrazit detaily filmu
  - [ ] název, žánr,...
- [ ] 3 práce s filmem v databázi
  - [ ] přidání nového filmu
  - [ ] editace filmu
  - [ ] mazání filmu 
- [ ] 4 zobrazit seznam herců a režisérů
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

## Databáze
- [x] Genre
  - [x] name (String) 

- [ ] Country
  - [ ] name (String) 
  - [ ] flag (Image) 

- [ ] Creator
  - [ ] name (String)
  - [ ] surname (String)
  - [ ] country (-> Country)
  - [ ] date_of_birth (Date)
  - [ ] date_of_death (Date)
  - [ ] biography (String) 
  - [ ] awards (n:m -> ??)
  - [ ] acting (n:m -> Movie)
  - [ ] directing (n:m -> Movie) 

- [ ] Movie
  - [ ] title_orig (String)
  - [ ] title_cz (String)
  - [ ] genres (n:m -> Genre)
  - [ ] countries (n:m -> Country)
  - [ ] length (Integer)
  - [ ] actors (n:m -> Creator)
  - [ ] directors (n:m -> Creator)
  - [ ] description (String)
  - [ ] released_date (Date)
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
