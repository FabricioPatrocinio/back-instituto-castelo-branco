from datetime import datetime
from uuid import uuid4

from pynamodb.attributes import BooleanAttribute, UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.models import Model
from settings import EnviromentEnum, settings

environment = settings.ENVIROMENT


class EnrollmentModel(Model):
    class Meta:
        table_name = f"EnrollmentModel{environment.capitalize()}"

    id = UnicodeAttribute(hash_key=True, default_for_new=str(uuid4()))
    active = BooleanAttribute(default=False)
    created_at = UTCDateTimeAttribute(default_for_new=datetime.utcnow())
    updated_at = UTCDateTimeAttribute(default=datetime.utcnow())
    emails = UnicodeAttribute()
    value = UnicodeAttribute()
    title = UnicodeAttribute()
    paragraph = UnicodeAttribute()
    expires_at = UTCDateTimeAttribute()
    created_at = UTCDateTimeAttribute(default_for_new=datetime.utcnow())
    updated_at = UTCDateTimeAttribute(default=datetime.utcnow())


class EnrollmentStudentModel(Model):
    class Meta:
        table_name = f"EnrollmentStudentModel{environment.capitalize()}"

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
    financial_responsible_name = UnicodeAttribute()
    financial_responsible_cpf = UnicodeAttribute()
    created_at = UTCDateTimeAttribute(default_for_new=datetime.utcnow())
    updated_at = UTCDateTimeAttribute(default=datetime.utcnow())


if environment == EnviromentEnum.TEST:
    if not EnrollmentModel.exists():
        EnrollmentModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)

    if not EnrollmentStudentModel.exists():
        EnrollmentStudentModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
