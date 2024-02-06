from datetime import datetime
from uuid import uuid4

from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.indexes import AllProjection, LocalSecondaryIndex
from pynamodb.models import Model
from settings import EnviromentEnum, settings

environment = settings.ENVIROMENT


class EmailIndex(LocalSecondaryIndex):
    class Meta:
        index_name = "email-index"
        read_capacity_units = 1
        write_capacity_units = 1
        projection = AllProjection()

    email = UnicodeAttribute(hash_key=True)


class UserModel(Model):
    class Meta:
        table_name = f"UserModel{environment.capitalize()}"

    id = UnicodeAttribute(hash_key=True, default_for_new=str(uuid4()))
    name = UnicodeAttribute()
    email = UnicodeAttribute()
    password = UnicodeAttribute()
    phone = UnicodeAttribute()
    created_at = UTCDateTimeAttribute(default_for_new=datetime.utcnow())
    updated_at = UTCDateTimeAttribute(default=datetime.utcnow())

    email_index = EmailIndex()


if environment == EnviromentEnum.TEST:
    if not UserModel.exists():
        UserModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
