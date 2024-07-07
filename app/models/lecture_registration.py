from datetime import datetime
from uuid import uuid4

from models import create_table
from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.models import Model
from settings import settings

environment = settings.ENVIROMENT


class LectureRegistrationModel(Model):
    class Meta:
        table_name = f"LectureRegistrationModel{environment.capitalize()}"

    id = UnicodeAttribute(hash_key=True, default_for_new=str(uuid4()))
    name = UnicodeAttribute()
    address = UnicodeAttribute()
    email = UnicodeAttribute()
    phone = UnicodeAttribute()
    student_cpf = UnicodeAttribute()
    student_rg = UnicodeAttribute()
    status_student = UnicodeAttribute()
    school_name = UnicodeAttribute()
    birth_date = UTCDateTimeAttribute()
    created_at = UTCDateTimeAttribute(default_for_new=datetime.utcnow())
    updated_at = UTCDateTimeAttribute(default=datetime.utcnow())


create_table(LectureRegistrationModel)
