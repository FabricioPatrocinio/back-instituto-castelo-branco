from datetime import datetime

from models.registration import RegistrationModel
from schemas.registration import RegistrationBaseSchema, RegistrationSchema


def update_registration(data: RegistrationBaseSchema) -> RegistrationSchema:
    model = RegistrationModel.get(hash_key=str(data.id))

    model.update(
        actions=[
            RegistrationModel.active.set(True),
            RegistrationModel.updated_at.set(datetime.utcnow()),
        ]
    )

    return model.to_simple_dict()
