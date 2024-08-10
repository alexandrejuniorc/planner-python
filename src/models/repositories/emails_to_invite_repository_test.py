import pytest
import uuid

from src.models.settings.db_connection_handler import db_connection_handler
from .emails_to_invite_repository import EmailsToInviteRepository

db_connection_handler.connect()
trip_id = str(uuid.uuid4())
email = "johndoe@mail.com"


@pytest.mark.skip(
    reason="Interaction with the database is not recommended in unit tests."
)
def test_register_email():
    connection = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(connection)

    emails_to_invite_repository.register_email(
        {"id": str(uuid.uuid4()), "trip_id": trip_id, "email": email}
    )


@pytest.mark.skip(
    reason="Interaction with the database is not recommended in unit tests."
)
def test_find_emails_from_trip():
    connection = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(connection)

    emails = emails_to_invite_repository.find_emails_from_trip(trip_id)
    print(emails)
