from aws_lambda_powertools.event_handler import APIGatewayRestResolver

from . import publications, registration

app = APIGatewayRestResolver(enable_validation=True)

app.enable_swagger(path="/swagger")

app.include_router(publications.router, prefix="/publications")
app.include_router(registration.router, prefix="/registration")
