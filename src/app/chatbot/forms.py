from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length

class CreateUpdatePromptForm(FlaskForm):
    prompt = StringField('Prompt', validators=[DataRequired(), Length(min=1)])
