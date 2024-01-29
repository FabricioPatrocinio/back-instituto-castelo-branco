from datetime import datetime
from uuid import uuid4

from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.models import Model
from settings import EnviromentEnum, settings

environment = settings.ENVIROMENT


class PublicationsModel(Model):
    class Meta:
        table_name = f"PublicationsModel{environment.capitalize()}"

    id = UnicodeAttribute(hash_key=True, default_for_new=str(uuid4()))
    title = UnicodeAttribute()
    paragraph = UnicodeAttribute()
    file_path = UnicodeAttribute(null=True)
    created_at = UTCDateTimeAttribute(default_for_new=datetime.utcnow())
    updated_at = UTCDateTimeAttribute(default=datetime.utcnow())


if environment == EnviromentEnum.TEST:
    if not PublicationsModel.exists():
        PublicationsModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
