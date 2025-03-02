from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from database import db
from models import EmailCadastro
from schemas import EmailCadastroSchema
from faker import Faker

app = Flask(__name__)

# Configuração do Banco de Dados SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializar Banco e Serializador
db.init_app(app)
ma = Marshmallow(app)
email_schema = EmailCadastroSchema()
emails_schema = EmailCadastroSchema(many=True)

# Criar tabelas e popular com dados fake
with app.app_context():
    db.create_all()
    if not EmailCadastro.query.first():
        fake = Faker()
        for _ in range(5):
            novo_email = EmailCadastro(email=fake.email(), status="pendente")
            db.session.add(novo_email)
        db.session.commit()

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API de Cadastro de E-mails para Faturas"})

@app.route("/cadastrar-email", methods=["POST"])
def cadastrar_email():
    data = request.get_json()
    email = data.get("email")

    if EmailCadastro.query.filter_by(email=email).first():
        return jsonify({"message": "E-mail já cadastrado"}), 400

    novo_email = EmailCadastro(email=email)
    db.session.add(novo_email)
    db.session.commit()

    return jsonify({"message": "E-mail cadastrado com sucesso", "email": novo_email.email}), 201

@app.route("/listar-emails", methods=["GET"])
def listar_emails():
    emails = EmailCadastro.query.all()
    return emails_schema.jsonify(emails)

if __name__ == "__main__":
    app.run(debug=True)
