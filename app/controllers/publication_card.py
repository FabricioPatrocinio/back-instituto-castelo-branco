from uuid import uuid4

from aws_lambda_powertools.event_handler.exceptions import NotFoundError
from models import update_item
from models.publication_card import PublicationCardModel
from pynamodb.exceptions import DoesNotExist
from schemas.publication_card import (
    PublicationCardRequestSchema,
    PublicationCardResponseSchema,
    PublicationCardUpdateSchema,
)
from settings import settings
from utils.s3 import delete_image_from_s3


def create_publication_card(schema: PublicationCardRequestSchema) -> PublicationCardResponseSchema:
    schema.id = str(uuid4())
    model = PublicationCardModel(**schema.model_dump())

    model.save()

    return model.to_simple_dict()


def get_all_publication_cards(limit: int, page_size: int) -> list[PublicationCardResponseSchema]:
    model = PublicationCardModel.scan(limit=limit, page_size=page_size)

    return model


def get_publication_card(publication_id: str) -> PublicationCardResponseSchema | None:
    try:
        model = PublicationCardModel.get(publication_id)
    except DoesNotExist:
        raise NotFoundError("Publication card not found")

    return model.to_simple_dict()


def delete_publication_card(publication_id: str) -> None:
    try:
        model = PublicationCardModel.get(publication_id)
    except DoesNotExist:
        raise NotFoundError("Publication card not found")

    model.delete()

    delete_image_from_s3(settings.S3_BUCKET_NAME, model.img_name)


def update_publication_card(schema: PublicationCardUpdateSchema) -> PublicationCardResponseSchema:
    publication_card = update_item(model=PublicationCardModel, item_id=schema.id, update_values=schema.model_dump())
    model = PublicationCardModel.get(schema.id)

    new_image = model.img_name != schema.img_name
    if new_image:
        delete_image_from_s3(settings.S3_BUCKET_NAME, model.img_name)

    return publication_card
