from datetime import datetime
from uuid import uuid4

from models import create_table
from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.exceptions import PutError
from pynamodb.indexes import AllProjection, LocalSecondaryIndex
from pynamodb.models import Model
from settings import settings
from utils.exceptions import EmailAlreadyExistsError

environment = settings.ENVIROMENT


class EmailIndex(LocalSecondaryIndex):
    class Meta:
        index_name = "email-index"
        read_capacity_units = 1
        write_capacity_units = 1
        projection = AllProjection()

    email = UnicodeAttribute(hash_key=True)


class UserModel(Model):
    class Meta:
        table_name = f"UserModel{environment.capitalize()}"

    id = UnicodeAttribute(hash_key=True, default_for_new=str(uuid4()))
    name = UnicodeAttribute()
    email = UnicodeAttribute()
    password = UnicodeAttribute()
    phone = UnicodeAttribute()
    created_at = UTCDateTimeAttribute(default_for_new=datetime.utcnow())
    updated_at = UTCDateTimeAttribute(default=datetime.utcnow())

    email_index = EmailIndex()

    @classmethod
    def create_unique(cls, **kwargs):
        email = kwargs.get("email")

        if cls.email_index.count(email) > 0:
            raise EmailAlreadyExistsError

        model = cls(**kwargs)

        try:
            model.save()
            return model
        except PutError as error:
            raise error


create_table(UserModel)
