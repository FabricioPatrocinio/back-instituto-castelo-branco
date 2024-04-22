import json

from main import lambda_handler

from tests.data.apigw_event import apigw_event


def test_api_publications_create(lambda_context) -> None:
    event_data = apigw_event(path="/publications/create")

    ret = lambda_handler(event_data, lambda_context)
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "message" in ret["body"]
    assert data["message"] == "hello world"


def test_api_enrollment_create(lambda_context):
    event_data = apigw_event(path="/enrollment/create")

    ret = lambda_handler(event_data, lambda_context)
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "message" in ret["body"]
    assert data["message"] == "hello world"
