from models import BaseModel, create_table
from pynamodb.attributes import NumberAttribute, UnicodeAttribute
from settings import settings

environment = settings.ENVIROMENT


class TopicsModel(BaseModel):
    class Meta:
        table_name = f"TopicsModel{environment.capitalize()}"

    id = UnicodeAttribute(hash_key=True)
    title = UnicodeAttribute()
    order_sequence = NumberAttribute()


create_table(TopicsModel)
