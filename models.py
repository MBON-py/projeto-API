from database import db

class EmailCadastro(db.Model):
    __tablename__ = "emails"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    status = db.Column(db.String(20), default="pendent") # "pendente", "confirmado", "cancelado"

