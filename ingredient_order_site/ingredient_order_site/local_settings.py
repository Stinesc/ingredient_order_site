import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ingredient_order_site_db',
        'USER': 'ingredient_order_site_db_admin',
        'PASSWORD': '123',
        'HOST': '127.0.0.1',
        'PORT': 5432
    }
}