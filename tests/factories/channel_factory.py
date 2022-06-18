import factory
from faker import Faker

from app.models import Channel
from app.extensions import db

fake = Faker()

class ChannelFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Channel
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"

    name = fake.name()
    url = fake.url()
    description = fake.paragraph()
    country = 'br'
    image = b'marcuspereira.jpg'
    video = fake.url()