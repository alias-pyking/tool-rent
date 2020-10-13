# KeepBorrowUse
College Major project, a mvp for a toolrenting app

# Run locally
```
$ git clone https://github.com/shubhamsks/tool-rent.git
$ cd tool-rent
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ cd tool_rent
$ touch .env
```
#### Add following lines to .env file you just created
```
SECRET_KEY=<django_secret_key>
DEBUG=<True for local, False for production>
DATABASE_USER=toolrentuser # you can change it
DATABASE_PASSWORD=toolrentpassword # you can change it 
```
#### Install Postgres on your machine (google please)

```
$ sudo su - postgres
$ psql
# CREATE DATABASE tool_rent;
# CREATE ROLE toolrentuser WITH PASSWORD 'toolrentpassword';
# ALTER ROLE toolrentuser SET client_encoding TO 'utf8';
# ALTER ROLE toolrentuser SET timezone TO 'Asia/Kolkata';
# GRANT ALL PRIVILEGES ON DATABASE tool_rent TO toolrentuser;
# \q
$ exit
$ python manage.py migrate
$ python manage.py runserver
```
