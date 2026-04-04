"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os
from app import app, DB
from flask import render_template, request, redirect, url_for, flash
from app.propertyform import AddNewProperty
from werkzeug.utils import secure_filename
from app.models import Property


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Britnie-Ann Gray") #Name changed from 'Mary Jane'

#Added routes to starter template
@app.route('/properties/create/') #Routing for the form page to add new properties
def create():
    form = AddNewProperty()

    if form.validate_on_submit():
        photo = form.Picture.data
        filename = secure_filename(photo.filename)

        #Saving Image to a path
        photoPath = os.path.join(app.static['UPLOAD_FOLDER'], filename)
        photo.save(photoPath)

        #Creating new propery object
        New_Property = Property(
        title = form.Title.data,
        bedrooms = form.Number_of_Bedrooms.data,
        bathrooms = form.Number_of_Bathrooms.data,
        location = form.Location.data,
        price = form.Price.data,
        property_type = form.Type.data,
        description = form.Description.data,
        photo = filename)

        #Saving new property to database
        DB.session.add(New_Property)
        DB.session.commit()

        flash('New property successfully added', 'success')

        return redirect(url_for('properties'))
    return render_template('create.html', form=form)

@app.route('/properties/') #Routing for the page to load all property listings
def properties():
    all_properties = Property.query.all()
    return render_template('properties.html', properties = all_properties)

app.route('/properties/<int: propertyid>/') #Routing for the page that only displays information on a selected property
def specificProperty(propertyid):
    property = Property.query.get_or_404(propertyid)
    return render_template('property.html', property=property)


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
