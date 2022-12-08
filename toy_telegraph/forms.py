from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import DataRequired
from flask_mdeditor import  MDEditorField

class PostForm(FlaskForm):
    content = MDEditorField('Body', validators=[DataRequired()])
    submit = SubmitField()