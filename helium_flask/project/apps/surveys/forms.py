from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FieldList, FormField


class TextInput(FlaskForm):
    input_field = StringField()

class SelectionInput(FlaskForm):
    input_field = SelectField(coerce=int)

class SurveyQuestionForm(FlaskForm):
    label = StringField()
    selection_fields = FieldList(FormField(SelectionInput))
    text_fields = FieldList(FormField(TextInput))

    # def __init__(self):

