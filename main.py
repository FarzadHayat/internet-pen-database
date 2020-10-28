import os
import secrets
from flask import Flask, render_template, abort, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import models
from forms import Search, Add_Brand

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pens.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.secret_key = 'crazyhorse'

db = SQLAlchemy(app)

WTF_CSRF_ENABLED = True
WTF_CSRF_SECRET_KEY = 'ludicrousmode'


# home page route
@app.route('/')
def home():
    brands = models.Brand.query.all()
    tags = models.Tag.query.all()
    return render_template('home.html', page_title='S', brands = brands, tags = tags)


# brand page route
@app.route('/brand/<int:id>')
def brand(id):
    brand = models.Brand.query.filter_by(id=id).first_or_404()
    return render_template('brand.html', page_title=' BRANDS', brand = brand)


# tag page route
@app.route('/tag/<int:id>')
def tag(id):
    tag = models.Tag.query.filter_by(id=id).first_or_404()
    return render_template('tag.html', page_title=' TAGS', tag = tag)


# pen page route
@app.route('/pen/<int:id>')
def pen(id):
    pen = models.Pen.query.filter_by(id=id).first_or_404()
    return render_template('pen.html', page_title=(' PENS'), pen = pen)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


# save brand photo to computer files
def save_photo(form_photo):
    # give the file a random name to prevent errors with similar file names already in the database
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_photo.filename)
    photo_fn = random_hex + f_ext
    # save the uploaded photo to the database
    photo_path = os.path.join(app.root_path, 'static', 'images', 'brands', photo_fn)
    form_photo.save(photo_path)
    return photo_fn


# delete brand photo from computer files
def delete_photo(form_photo):
    photo_path = os.path.join(app.root_path, 'static', 'images', 'brands', form_photo)
    os.remove(photo_path)
    return


# form to add a brand to the database
@app.route('/add_brand', methods = ['GET', 'POST'])
def add_brand():
    form = Add_Brand()
    # form submitted to the server by a user
    if form.validate_on_submit():
        new_brand = models.Brand()
        # set brand name and description from form data
        new_brand.name = form.name.data
        new_brand.desc = form.desc.data
        if form.photo.data:
            photo_file = save_photo(form.photo.data)
            new_brand.photo = photo_file
        new_brand.deletable = True
        # flash message to let user know that the brand has been created
        flash('{} brand successfully created.'.format(new_brand.name))
        db.session.add(new_brand)
        db.session.commit()
        return redirect(url_for('brand', id=new_brand.id))
    # request to see the page
    return render_template('add_edit_brand.html', form = form, title = "Add Brand", legend = "Add")


# form to edit a brand in the database
@app.route('/edit_brand/<int:id>', methods = ['GET', 'POST'])
def edit_brand(id):
    form = Add_Brand()
    # current brand data
    brand = db.session.query(models.Brand).filter(models.Brand.id==id).first_or_404()
    # form submitted to the server by a user
    if form.validate_on_submit():
        # set brand name and description from form data
        brand.name = form.name.data
        brand.desc = form.desc.data
        # check if user wants to update the brand photo
        if form.photo.data:
            # save new photo file
            photo_file = save_photo(form.photo.data)
            # delete old photo file
            delete_photo(brand.photo)
            # set new photo
            brand.photo = photo_file
        # flash message to let user know that the brand has been edited
        flash('{} brand successfully edited.'.format(brand.name))
        db.session.commit()
        return redirect(url_for('brand', id=brand.id))
    # populate fields with currently saved data
    form.name.data = brand.name
    form.desc.data = brand.desc
    # title for the edit page
    title = "Editing {} brand".format(brand.name)
    # request to see the page
    return render_template('add_edit_brand.html', form = form, title = title, legend = "Save")


# form to delete a brand from the database
@app.route('/delete_brand/<int:id>')
def delete_brand(id):
    brand = db.session.query(models.Brand).filter(models.Brand.id==id).first_or_404()
    # delete saved photo from files
    if brand.photo:
        photo_file = delete_photo(brand.photo)
    # flash message to let user know that the brand has been deleted
    flash('{} brand successfully deleted.'.format(brand.name))
    # delete brand from database
    db.session.delete(brand)
    db.session.commit()
    return redirect(url_for('home'))


# search form
@app.route('/search', methods = ['GET', 'POST'])
def search():
    form = Search()
    pens = models.Pen.query.all()
    brands = models.Brand.query.all()
    tags = models.Tag.query.all()
    # populate the dropdown selections
    form.brand.choices = [(brand.id, brand.name) for brand in brands]
    form.tag.choices = [(tag.id, tag.name) for tag in tags]

    selected_tag = form.tag.data
    selected_brand = form.brand.data

    # if no search done yet
    results = pens
    has_searched = False

    if request.method == 'POST':
        if form.validate_on_submit():
            has_searched = True
            brand = models.Brand.query.filter_by(id = selected_brand).first()
            tag = models.Tag.query.filter_by(id = selected_tag).first()
            # Get a list of the pens common between the brand and the tag chosen.
            results = list(set(brand.pens).intersection(tag.pens))
            # render the search results
            return render_template('search.html', title = "Find a Pen", form = form, results = results, brand = brand.name, tag = tag.name, has_searched = has_searched)
        else:
            abort(404)
    return render_template('search.html', title = "Find a Pen", form = form, results = results, has_searched = has_searched)

# credits page route
@app.route('/credits')
def credits():
    credits = models.Credit.query.all()
    return render_template('credits.html', page_title=' CREDITS', credits = credits)


if __name__ == "__main__":
    app.run(debug=True)
