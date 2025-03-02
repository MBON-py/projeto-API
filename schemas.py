from flask_marshmallow import Marshmallow
from models import EmailCadastro

ma = Marshmallow()

class EmailCadastroSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EmailCadastro