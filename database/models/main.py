from database import Database


def register_database_models() -> None:
    Database().BASE.metadata.create_all(Database().engine)
