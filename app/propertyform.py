from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, FileField, SubmitField
from wtforms.validators import InputRequired
from flask_wtf.file import FileRequired, FileAllowed

class AddNewProperty(FlaskForm):
    Title = StringField('Property Name', validators = [InputRequired()])
    Number_of_Bedrooms = StringField('Number of Bedrooms', validators = [InputRequired()])
    Number_of_Bathrooms = StringField('Number of Bathroomse', validators = [InputRequired()])
    Location = StringField('Address', validators = [InputRequired()])
    Price = StringField('Price', validators = [InputRequired()])
    Type = SelectField('Property Type', choices = [(House, House), (Apartment, Apartment)], validators = [InputRequired()])
    Description = TextAreaField('Description', validators = [InputRequired()])
    Picture = FileField('Photo', validators = [FileRequired(), FileAllowed(['jpeg', 'png', 'jpg'], 'Images only')])
    Submit = SubmitField('Add Property')