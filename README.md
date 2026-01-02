This project uses the following packages

djangorestframework
djangorestframework-simplejwt
dotenv
psycopg2
cryptography
django-filter
silk


Before running the application please use the following commands

1> To start the virtual environment
python3 -m venv env
source env/bin/activate

2> To install the dependencies
pip install djangorestframework djangorestframework-simplejwt dotenv psycopg2 cryptography django-filter silk

3> Drop into python shell and generate a cryptography.Fernet key

4> Add the generated key in core/.env file as

SUPER_SECRET_KEY

also add your postgresql database connectionstring as

DATABASE_URL

in the same file aswell

5> Run migrations
python3 manage.py makemigrations
python3 manage.py migrate

6> Start server
python3 manage.py runserver

