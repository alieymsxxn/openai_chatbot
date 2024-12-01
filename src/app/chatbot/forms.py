from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CreateUpdatePromptForm(FlaskForm):
    '''Form for creating or updating a prompt.

    This form includes a single field for the prompt text, which is required
    and must be at least one character long.
    '''
    prompt = StringField('Prompt', validators=[DataRequired(), Length(min=1)])
