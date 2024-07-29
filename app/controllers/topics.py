from uuid import uuid4

from aws_lambda_powertools.event_handler.exceptions import NotFoundError
from models.topics import TopicsModel
from pynamodb.exceptions import DoesNotExist
from schemas.topics import TopicsRequestSchema, TopicsResponseSchema, TopicsUpdateSchema
from utils import current_utc_time


def create_topics(schema: TopicsRequestSchema) -> TopicsResponseSchema:
    """Create the topic and sort based on the last in the list"""
    highest_order_sequence = 0

    if all_topics := list(TopicsModel.scan()):
        topics_sorted = sorted(all_topics, key=lambda x: x.order_sequence, reverse=True)
        highest_order_sequence = topics_sorted[0].order_sequence

    schema.id = str(uuid4())
    schema.order_sequence = highest_order_sequence + 1

    model = TopicsModel(**schema.model_dump())
    model.save()

    return model.to_simple_dict()


def get_all_topics(limit: int, page_size: int) -> list[TopicsResponseSchema]:
    model = TopicsModel.scan(limit=limit, page_size=page_size)

    if model:
        return sorted(list(model), key=lambda dic: dic.order_sequence)

    return model


def get_topics(topics_id: str) -> TopicsResponseSchema | None:
    try:
        model = TopicsModel.get(topics_id)
    except DoesNotExist:
        raise NotFoundError("Topics card not found")

    return model.to_simple_dict()


def delete_topics(topics_id: str) -> None:
    try:
        model = TopicsModel.get(topics_id)
    except DoesNotExist:
        raise NotFoundError("Topic card not found")

    model.delete()


def update_topics(schema: TopicsUpdateSchema) -> TopicsResponseSchema:
    """
    Update topic taking into account changes in sequence order, modifying if
    a topic is necessary to inherit the order of the updated one in question
    """
    primary_model = TopicsModel.get(str(schema.id))

    if schema.order_sequence and primary_model.order_sequence != schema.order_sequence:
        secondary_model = list(TopicsModel.scan(TopicsModel.order_sequence == schema.order_sequence))

        if secondary_model:
            secondary_model[0].order_sequence = primary_model.order_sequence
            secondary_model[0].updated_at = current_utc_time()
            secondary_model[0].save()

            primary_model.order_sequence = schema.order_sequence

    if title := schema.title:
        primary_model.title = title

    primary_model.updated_at = current_utc_time()
    primary_model.save()

    return primary_model.to_simple_dict()
