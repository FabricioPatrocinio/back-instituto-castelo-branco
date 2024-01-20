from datetime import datetime
from uuid import uuid4

from pynamodb.attributes import BooleanAttribute, UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.models import Model
from settings import settings


class RegistrationModel(Model):
    class Meta:
        table_name = f"RegistrationModel{settings.ENVIROMENT.capitalize()}"

    id = UnicodeAttribute(hash_key=True, default_for_new=str(uuid4()))
    active = BooleanAttribute(default=False)
    created_at = UTCDateTimeAttribute(default_for_new=datetime.utcnow())
    updated_at = UTCDateTimeAttribute(default=datetime.utcnow())


if not RegistrationModel.exists():
    RegistrationModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
