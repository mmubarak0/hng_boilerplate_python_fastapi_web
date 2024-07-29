# from setuptools import setup, find_packages
# setup(name='api', packages=find_packages())
import alembic.config
from sqlalchemy import create_engine
from decouple import config
from api.db.database import Base


DB_TYPE = config("DB_TYPE")
DB_NAME = config("DB_NAME")
DB_USER = config("DB_USER")
DB_PASSWORD = config("DB_PASSWORD")
DB_HOST = config("DB_HOST")
DB_PORT = config("DB_PORT")
MYSQL_DRIVER = config("MYSQL_DRIVER")
DATABASE_URL = ""

if MYSQL_DRIVER:
    DATABASE_URL = f'{DB_TYPE}+{MYSQL_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
else:
    DATABASE_URL = f'{DB_TYPE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


engine = create_engine(DATABASE_URL)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

alembicArgs = [
    '--raiseerr',
    'upgrade', 'head',
]

alembic.config.main(argv=alembicArgs)