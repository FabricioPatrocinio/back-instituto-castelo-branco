from datetime import datetime
from uuid import uuid4

from pynamodb.attributes import BooleanAttribute, ListAttribute, UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.models import Model
from settings import EnviromentEnum, settings

environment = settings.ENVIROMENT


class PublicationCardModel(Model):
    class Meta:
        table_name = f"PublicationCardModel{environment.capitalize()}"

    id = UnicodeAttribute(hash_key=True, default_for_new=str(uuid4()))
    active = BooleanAttribute(default=False)
    title = UnicodeAttribute()
    emails = ListAttribute(null=True, of=UnicodeAttribute)
    paragraph = UnicodeAttribute()
    img_id = UnicodeAttribute(null=True)
    link = UnicodeAttribute(null=True)
    expires_at = UTCDateTimeAttribute(null=True)
    created_at = UTCDateTimeAttribute(default_for_new=datetime.utcnow())
    updated_at = UTCDateTimeAttribute(default=datetime.utcnow())


if environment == EnviromentEnum.TEST:
    if not PublicationCardModel.exists():
        PublicationCardModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
