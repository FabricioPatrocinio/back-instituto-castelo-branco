from aws_lambda_powertools.event_handler import APIGatewayRestResolver

from . import enrollment, helpers, publications

app = APIGatewayRestResolver(enable_validation=True)

app.enable_swagger(path="/swagger")

app.include_router(helpers.router, prefix="/helpers")
app.include_router(publications.router, prefix="/publications")
app.include_router(enrollment.router, prefix="/enrollment")
