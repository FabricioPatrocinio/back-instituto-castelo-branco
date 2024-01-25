from models.publications import PublicationsModel
from schemas.publications import PublicationsBaseSchema, PublicationsSchema


def create_publication(data: PublicationsBaseSchema) -> PublicationsSchema:
    model = PublicationsModel(**data.model_dump(exclude_none=True))

    model.save()

    return model.to_simple_dict()


def get_publications(page_size: int) -> list[PublicationsSchema]:
    model = PublicationsModel.scan(limit=page_size, page_size=page_size)

    return model


def delete_publication(id: str) -> None:
    model = PublicationsModel.get(hash_key=id)
    model.delete()
