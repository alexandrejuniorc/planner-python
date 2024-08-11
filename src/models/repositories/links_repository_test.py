import pytest
import uuid

from src.models.settings.db_connection_handler import db_connection_handler
from .links_repository import LinksRepository

db_connection_handler.connect()
trip_id = str(uuid.uuid4())
link_id = str(uuid.uuid4())
email = "johndoe@mail.com"


@pytest.mark.skip(
    reason="Interaction with the database is not recommended in unit tests."
)
def test_register_link():
    connection = db_connection_handler.get_connection()
    links_repository = LinksRepository(connection)

    links_repository.register_link(
        {
            "id": link_id,
            "trip_id": trip_id,
            "link": "https://www.google.com",
            "title": "Google",
        }
    )


@pytest.mark.skip(
    reason="Interaction with the database is not recommended in unit tests."
)
def test_find_links_from_trip():
    connection = db_connection_handler.get_connection()
    links_repository = LinksRepository(connection)

    links = links_repository.find_links_from_trip(trip_id)
    print(links)
