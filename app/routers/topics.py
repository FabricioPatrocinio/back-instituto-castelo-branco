from aws_lambda_powertools.event_handler.exceptions import NotFoundError
from aws_lambda_powertools.event_handler.router import APIGatewayRouter
from controllers.topics import create_topics, delete_topics, get_all_topics, get_topics, update_topics
from schemas.topics import TopicsRequestSchema, TopicsResponseSchema, TopicsUpdateSchema
from utils.jwt import JwtAuthMiddleware
from utils.logger import logger
from utils.tracer import tracer

router = APIGatewayRouter()
tags = ["Topics"]


@router.post(rule="/", tags=tags, summary="Cria um topico", middlewares=[JwtAuthMiddleware()])
@tracer.capture_method
def _create_topics(body: TopicsRequestSchema) -> TopicsResponseSchema:
    # TODO: Implementar o auth no swagger, pois a lib nao faz automaticamente
    # REF: https://docs.powertools.aws.dev/lambda/python/latest/core/event_handler/api_gateway/#customizing_api_metadatapy
    logger.info(body.model_dump)

    return create_topics(body)


@router.put(
    rule="/",
    tags=tags,
    summary="Atualiza um topico",
    middlewares=[JwtAuthMiddleware()],
)
@tracer.capture_method
def _update_topics(body: TopicsUpdateSchema) -> TopicsResponseSchema:
    logger.info(body.model_dump)

    return update_topics(body)


@router.get(
    rule="/id/<id>",
    tags=tags,
    summary="Pega um topico",
    middlewares=[JwtAuthMiddleware()],
)
@tracer.capture_method
def _get_topics(id: str) -> TopicsResponseSchema:
    if data := get_topics(id):
        return data

    raise NotFoundError("Topics card not found")


@router.get(
    rule="/get-all/limit/<limit>/page-size/<page_size>",
    tags=tags,
    summary="Pega todos os topicos por tamanho de paginacao",
)
@tracer.capture_method
def _get_all_topics(limit: int, page_size: int) -> list[TopicsResponseSchema]:
    topics = get_all_topics(limit, page_size)

    return topics


@router.delete(rule="/topic-id/<topic_id>", tags=tags, summary="Deleta topicos", middlewares=[JwtAuthMiddleware()])
@tracer.capture_method
def _delete_topics(topic_id: str) -> None:
    return delete_topics(topic_id)
