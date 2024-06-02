from datetime import datetime

from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.models import Model
from settings import EnviromentEnum, settings

environment = settings.ENVIROMENT


class PublicationCardModel(Model):
    class Meta:
        table_name = f"PublicationCardModel{environment.capitalize()}"

    id = UnicodeAttribute(hash_key=True)
    title = UnicodeAttribute()
    paragraph = UnicodeAttribute()
    img_name = UnicodeAttribute(null=True)
    link = UnicodeAttribute(null=True)
    text_button_submit = UnicodeAttribute(null=True)
    created_at = UTCDateTimeAttribute(default_for_new=datetime.utcnow())
    updated_at = UTCDateTimeAttribute(default=datetime.utcnow())


if environment == EnviromentEnum.TEST:
    if not PublicationCardModel.exists():
        PublicationCardModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
