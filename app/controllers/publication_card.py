from aws_lambda_powertools.event_handler.exceptions import NotFoundError
from models import update_item
from models.publication_card import PublicationCardModel
from pynamodb.exceptions import DoesNotExist
from schemas.publication_card import (
    PublicationCardRequestSchema,
    PublicationCardResponseSchema,
    PublicationCardUpdateSchema,
)


def create_publication_card(data: PublicationCardRequestSchema) -> PublicationCardResponseSchema:
    model = PublicationCardModel(**data.model_dump())

    model.save()

    return model.to_simple_dict()


def get_all_publication_cards(limit: int, page_size: int) -> list[PublicationCardResponseSchema]:
    model = PublicationCardModel.scan(limit=limit, page_size=page_size)

    return model


def get_publication_card(id: str) -> PublicationCardResponseSchema | None:
    try:
        model = PublicationCardModel.get(id)
    except DoesNotExist:
        raise NotFoundError("Publication card not found")

    return model.to_simple_dict()


def delete_publication_card(id: str) -> None:
    model = PublicationCardModel.get(id=id)

    model.delete()


def update_publication_card(data: PublicationCardUpdateSchema) -> PublicationCardResponseSchema:
    publication_card = update_item(model=PublicationCardModel, item_id=data.id, update_values=data.model_dump())

    return publication_card
