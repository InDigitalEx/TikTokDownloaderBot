from typing import Final

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from utils import SingletonMeta, get_root_dir


class Database(metaclass=SingletonMeta):
    BASE: Final = declarative_base()

    def __init__(self):
        root_dir = get_root_dir()
        self._engine = create_engine(f'sqlite+pysqlite:///{root_dir}/database.db', echo=True)
        session = sessionmaker(bind=self._engine)
        self._session = session()

    @property
    def session(self):
        return self._session

    @property
    def engine(self):
        return self._engine
