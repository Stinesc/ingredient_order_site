# Ingredient order site

## How to run

#### Clone project:
```bash
git clone https://github.com/Stinesc/ingredient_order_site.git
```
#### Install PostgreSQL:
```bash
sudo apt-get install postgresql
```
#### Start PostgreSQL console:
```bash
sudo -u postgres psql
```
#### Create database and user:
```bash
CREATE DATABASE ingredient_order_site_db;
CREATE USER ingredient_order_site_db_admin WITH PASSWORD '123';
ALTER USER ingredient_order_site_db_admin CREATEDB; (for tests)
CTRL + D
```
#### Run with Docker:
```bash
sudo docker-compose run web python3 manage.py migrate
sudo docker-compose run web python3 manage.py createsuperuser
sudo docker-compose up
```
#### Run tests:
```bash
python3 manage.py test
```