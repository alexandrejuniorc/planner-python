from sqlite3 import Connection
from typing import Dict, Tuple


class EmailsToInviteRepository:
    def __init__(self, connection: Connection) -> None:
        self.__connection = connection

    def register_email(self, email_infos: Dict) -> None:
        cursor = self.__connection.cursor()
        cursor.execute(
            """
            INSERT INTO emails_to_invite (id, trip_id, email)
            VALUES (?, ?, ?)
            """,
            (
                email_infos["id"],
                email_infos["trip_id"],
                email_infos["email"],
            ),
        )
        self.__connection.commit()

    def find_emails_from_trip(self, trip_id: str) -> list[Tuple]:
        cursor = self.__connection.cursor()
        cursor.execute(
            """
            SELECT * FROM emails_to_invite WHERE trip_id = ?
            """,
            (trip_id,),
        )
        trip = cursor.fetchall()
        return trip
