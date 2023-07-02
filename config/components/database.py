import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('PGDB_DEFAULT_DB_NAME'),
        'USER': os.environ.get('PGDB_DEFAULT_USER_NAME'),
        'PASSWORD': os.environ.get('PGDB_DEFAULT_PASSWORD'),
        'HOST': os.environ.get('PGDB_DEFAULT_HOST_NAME'),
        'PORT': os.environ.get('PGDB_DEFAULT_PORT'),
    },
    'store': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('PGDB_STORE_DB_NAME'),
        'USER': os.environ.get('PGDB_STORE_USER_NAME'),
        'PASSWORD': os.environ.get('PGDB_STORE_PASSWORD'),
        'HOST': os.environ.get('PGDB_STORE_HOST_NAME'),
        'PORT': os.environ.get('PGDB_STORE_PORT'),
    },
    'warehouse': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('PGDB_WAREHOUSE_DB_NAME'),
        'USER': os.environ.get('PGDB_WAREHOUSE_USER_NAME'),
        'PASSWORD': os.environ.get('PGDB_WAREHOUSE_PASSWORD'),
        'HOST': os.environ.get('PGDB_WAREHOUSE_HOST_NAME'),
        'PORT': os.environ.get('PGDB_WAREHOUSE_PORT'),
    }
}

DATABASE_ROUTERS = [
    'config.db_routers.main_router.MainRouter',
]
