Summer for Progress
=========================

* [What is this?](#what-is-this)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Usage & Useful Commands](#usage-&-useful-commands)

What is this?
-------------------
The official website for the Summer for Progress, a campaign organized by progressive groups across the country to demand House Democrats cosponsor a people’s platform – 8 bills that say definitively people over profit.

Prerequisites
-------------------
1. [Python 2.7](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installing/)
2. [PostgreSQL](https://www.postgresql.org/download/) – If you have [homebrew](https://brew.sh/), simply `brew install postgresql`
3. **Recommended** - [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
4. [Node + NPM](https://nodejs.org/en/download/) for building front-end. 

Installation
-------------------
Clone this repository and navigate to the project directory.
```
git clone git@github.com:Our-Revolution/summer-for-progress.git summerforprogress
cd summerforprogress
```
Optionally (but recommended), make a [virtualenv](https://pypi.python.org/pypi/virtualenv) and activate it using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/).
```
mkvirtualenv summerforprogress
workon summerforprogress
```
Install required packages.
```
pip install -r requirements.txt
```

Create a PostgreSQL database with the PostGIS extension and add the database URL to your .env file. 
```
local here=${PWD##*/};
createuser "$here" && createdb -O"$here" -Eutf8 "$here" && echo "DATABASE_URL=postgis://$here@localhost:5432/$here" >> .env && echo "CREATE EXTENSION postgis;" | psql -U superuser "$here";
```

**Note:** Add the [following gist](https://gist.github.com/cjmabry/c78f40ae772a742deaa193f3c1534532) to your .bash_profile or .zshrc to easily create project databases.

Install front-end dependencies.
```
npm install
```

Run initial database migrations.
```
./manage.py migrate
```
Run the development server.
```
./manage runserver
```

Importing representatives
---------------------------
The Summer for Progress site contains a scorecard to monitor elected officials stances on the various bills inside the People's Platform.

To quickly import starting data for these representatives, use the CSV importer functionality in the django admin.

Visit [http://localhost:8000/admin/](http://localhost:8000/admin/), and add and save a new CSV import, using `summerforprogress.Representative` as the model name and `data/initial_data.csv` as the upload file.

Usage & Useful Commands
-------------------
From the working directory:

```
# Create an Admin User
python manage.py createsuperuser

# Run Local Server
python manage.py runserver

# Make Migrations
python manage.py makemigrations

# Run Migrations
python manage.py migrate
```
