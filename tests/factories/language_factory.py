import factory
from faker import Faker

from app.models import Language
from app.extensions import db

fake = Faker()

class LanguageFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Language
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"

    name = fake.name()
