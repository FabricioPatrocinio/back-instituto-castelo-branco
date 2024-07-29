from typing import TypeVar

from pynamodb.attributes import UTCDateTimeAttribute
from pynamodb.models import Model
from settings import EnviromentEnum, settings
from utils import current_utc_time

environment = settings.ENVIROMENT

ModelPynamodb = TypeVar("ModelPynamodb", bound=Model)


class BaseModel(Model):
    created_at = UTCDateTimeAttribute(default_for_new=current_utc_time)
    updated_at = UTCDateTimeAttribute(default=current_utc_time)


def update_item(model: ModelPynamodb, item_id: str, update_values: dict) -> dict:
    item = model.get(item_id)

    for key, value in update_values.items():
        if key != "id" and value:
            setattr(item, key, value)

    item.updated_at = current_utc_time()

    item.save()

    return item.to_simple_dict()


def create_table(model: ModelPynamodb):
    if environment != EnviromentEnum.TEST:
        return

    if not model.exists():
        model.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
