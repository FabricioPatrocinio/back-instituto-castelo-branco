from datetime import datetime
from typing import TypeVar

from pynamodb.models import Model

ModelPynamodb = TypeVar("ModelPynamodb", bound=Model)


def update_item(model: ModelPynamodb, item_id: str, update_values: dict) -> dict:
    item = model.get(item_id)

    for key, value in update_values.items():
        if value is not None:
            setattr(item, key, value)

    item.updated_at = datetime.utcnow()

    item.save()

    return item.to_simple_dict()
