import sqlite3
from sqlite3 import Connection


class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "storage.db"
        self.__connection = None

    def connect(self) -> None:
        self.__connection = sqlite3.connect(
            self.__connection_string, check_same_thread=False
        )

    def get_connection(self) -> Connection:
        return self.__connection

    def disconnect(self) -> None:
        self.__connection.close()


db_connection_handler = DBConnectionHandler()
