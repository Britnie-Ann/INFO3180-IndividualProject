from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, FileField, SubmitField
from wtforms.validators import InputRequired
from flask_wtf.file import FileRequired, FileAllowed

class AddNewProperty(FlaskForm):
    Title = StringField('Property Title', validators = [InputRequired()])
    Number_of_Bedrooms = StringField('No. of Rooms', validators = [InputRequired()])
    Number_of_Bathrooms = StringField('No. of Bathrooms', validators = [InputRequired()])
    Location = StringField('Location', validators = [InputRequired()])
    Price = StringField('Price', validators = [InputRequired()])
    Type = SelectField('Property Type', choices = [('', 'Please select'), ('house', 'House'), ('apartment', 'Apartment')], validators = [InputRequired()])
    Description = TextAreaField('Description', validators = [InputRequired()])
    Picture = FileField('Photo', validators = [FileRequired(), FileAllowed(['jpeg', 'png', 'jpg'], 'Images only')])
    Submit = SubmitField('Add Property')