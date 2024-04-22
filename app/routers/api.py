from aws_lambda_powertools.event_handler import APIGatewayRestResolver, CORSConfig

from . import auth, enrollment_student, helpers, lecture_registration, publication_card, publications

cors_config = CORSConfig(allow_origin="*", allow_headers=["Content-Type", "Authorization"], max_age=300)

app = APIGatewayRestResolver(cors=cors_config, enable_validation=True)

app.enable_swagger(path="/swagger")

app.include_router(helpers.router, prefix="/helpers")
app.include_router(publications.router, prefix="/publications")
app.include_router(publication_card.router, prefix="/publication-card")
app.include_router(enrollment_student.router, prefix="/enrollment-student")
app.include_router(lecture_registration.router, prefix="/lecture-registration")
app.include_router(auth.router, prefix="/auth")
