from datetime import datetime

from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.models import Model
from settings import EnviromentEnum, settings

environment = settings.ENVIROMENT


class UserModel(Model):
    class Meta:
        table_name = f"UserModel{environment.capitalize()}"

    id = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute()
    email = UnicodeAttribute()
    password = UnicodeAttribute()
    phone = UnicodeAttribute()
    created_at = UTCDateTimeAttribute(default_for_new=datetime.utcnow())
    updated_at = UTCDateTimeAttribute(default=datetime.utcnow())


if environment == EnviromentEnum.TEST:
    if not UserModel.exists():
        UserModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
