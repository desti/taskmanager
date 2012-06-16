from global_settings import *

ADMINS = (
    ('Stefan Grosz','stefan@grosz.at'),
)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'ait_app',                      # Or path to database file if using sqlite3.
        'USER': 'ait_app',                      # Not used with sqlite3.
        'PASSWORD': 'ait_app',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}