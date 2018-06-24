from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField
from wtforms.validators import DataRequired, Length

class SetTotp(FlaskForm):
    totp_code = StringField('TOTP Code',
                            validators=[DataRequired(), Length(min=6,max=6)])
    submit = SubmitField('Validar')
