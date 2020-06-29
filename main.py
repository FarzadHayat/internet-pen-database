from flask import Flask, render_template, abort, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import Select_Movie
import models

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pens.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.secret_key = 'bigrabbit'

db = SQLAlchemy(app)

WTF_CSRF_ENABLED = True
WTF_CSRF_SECRET_KEY = 'smallrabbit'

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
    return render_template('tag.html', page_title=' TAGS')

# pen page route
@app.route('/pen/<int:id>')
def pen(id):
    return render_template('pen.html', page_title=())

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == "__main__":
    app.run(debug=True)
