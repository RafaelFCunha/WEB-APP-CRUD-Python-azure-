from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class CadastroForm(FlaskForm):
    nome = StringField('Nome', [DataRequired()])
    sobrenome = StringField('Sobrenome', [DataRequired()])
    email = StringField('Email', [Email(message=('Not a valid email address.')), DataRequired()])
    endereco1 = StringField('Endereço 1', [DataRequired()])
    endereco2 = StringField('Endereço 2', [DataRequired()])
    submit = SubmitField('Submit')
