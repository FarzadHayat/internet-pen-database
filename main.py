from flask import Flask, render_template, abort, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import Select_Pen
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
    tag = models.Tag.query.filter_by(id=id).first_or_404()
    return render_template('tag.html', page_title=' TAGS', tag = tag)

# pen page route
@app.route('/pen/<int:id>')
def pen(id):
    pen = models.Pen.query.filter_by(id=id).first_or_404()
    return render_template('pen.html', page_title=(' PENS '), pen = pen)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

# dropdown list form
@app.route('/choose_pen', methods = ['GET', 'POST'])
def choose_pen():
    form = Select_Pen()
    pens = models.Pen.query.all()
    form.pens.choices = [(pen.id, pen.name) for pen in pens]
    if request.method == 'POST':
        if form.validate_on_submit():
            return redirect(url_for('pen', id = form.pens.data))
        else:
            abort(404)
            # uses a premade template. pen.html ????
    return render_template('pen.html', name = 'Select A Pen', form = form)

if __name__ == "__main__":
    app.run(debug=True)
