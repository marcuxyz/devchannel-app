from app.extensions import db

class Channel(db.Model):
    __tablename__ = "channels"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    url = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.Text)
    country = db.Column(db.String(5), nullable=False)
    video = db.Column(db.String)
    image = db.Column(db.LargeBinary)
    language_id = db.Column(db.Integer, db.ForeignKey('languages.id'))

    def __repr__(self) -> str:
        return self.name

class Language(db.Model):
    __tablename__ = "languages"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    channels = db.relationship('Channel', backref='language')

    def __repr__(self) -> str:
        return self.name
