from . import DB

class Property(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    title = DB.Column(DB.String(100), nullable=False)
    bedrooms = DB.Column(DB.Integer, nullable=False)
    bathrooms = DB.Column(DB.Integer, nullable=False)
    location = DB.Column(DB.String(100), nullable=False)
    price = DB.Column(DB.Float, nullable=False)
    property_type = DB.Column(DB.String(20), nullable=False)
    description = DB.Column(DB.Text, nullable=False)
    photo = DB.Column(DB.String(255), nullable=False)