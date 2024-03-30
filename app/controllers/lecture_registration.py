from models.lecture_registration import LectureRegistrationModel
from schemas.lecture_registration import LectureRegistrationRequestSchema, LectureRegistrationResponseSchema
from utils.emails.lecture_registration import send_email_with_html_template


def create_lecture_registration(data: LectureRegistrationRequestSchema) -> LectureRegistrationResponseSchema:
    model = LectureRegistrationModel(**data.model_dump())

    model.save()

    send_email_with_html_template(model.to_simple_dict())

    return model.to_simple_dict()
