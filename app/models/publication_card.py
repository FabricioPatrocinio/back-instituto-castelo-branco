from models import create_table
from pynamodb.attributes import BooleanAttribute, UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.models import Model
from settings import settings
from utils import current_utc_time

environment = settings.ENVIROMENT


class PublicationCardModel(Model):
    class Meta:
        table_name = f"PublicationCardModel{environment.capitalize()}"

    id = UnicodeAttribute(hash_key=True)
    topic = UnicodeAttribute(null=True)
    title = UnicodeAttribute(null=True)
    paragraph = UnicodeAttribute(null=True)
    img_name = UnicodeAttribute(null=True)
    link = UnicodeAttribute(null=True)
    is_internal_link = BooleanAttribute(null=True, default=True)
    is_form_with_responsible = BooleanAttribute(null=True)
    text_button_submit = UnicodeAttribute(null=True)
    created_at = UTCDateTimeAttribute(default_for_new=current_utc_time)
    updated_at = UTCDateTimeAttribute(default=current_utc_time)


create_table(PublicationCardModel)
