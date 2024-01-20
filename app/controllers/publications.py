from models.publications import PublicationsModel
from schemas.publications import PublicationsBaseSchema, PublicationsSchema


def create_publication(data: PublicationsBaseSchema) -> PublicationsSchema:
    model = PublicationsModel(**data.model_dump(exclude_none=True))

    model.save()

    return model.to_simple_dict()
