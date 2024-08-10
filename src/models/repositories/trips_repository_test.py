import pytest
import uuid
from datetime import datetime, timedelta

from src.models.settings.db_connection_handler import db_connection_handler

from .trips_repository import TripsRepository

db_connection_handler.connect()
trip_id = str(uuid.uuid4())


@pytest.mark.skip(
    reason="Interaction with the database is not recommended in unit tests."
)
def test_create_trip():
    connection = db_connection_handler.get_connection()
    trips_repository = TripsRepository(connection)

    trips_repository.create_trip(
        {
            "id": trip_id,
            "destination": "São Paulo",
            "start_date": datetime.strptime("02-01-2024", "%d-%m-%Y"),
            "end_date": datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
            "owner_name": "John Doe",
            "owner_email": "johndoe@mail.com",
        }
    )


@pytest.mark.skip(
    reason="Interaction with the database is not recommended in unit tests."
)
def test_find_trip_by_id():
    connection = db_connection_handler.get_connection()
    trips_repository = TripsRepository(connection)

    trip = trips_repository.find_trip_by_id(trip_id)
    print(trip)


@pytest.mark.skip(
    reason="Interaction with the database is not recommended in unit tests."
)
def test_update_trip_status():
    connection = db_connection_handler.get_connection()
    trips_repository = TripsRepository(connection)

    trips_repository.update_trip_status(trip_id)
