from flask-wtf import FlaskForm
from wtforms import SelectField
from wtforms.validators import DataRequired

class Select_Pen(FlaskForm):
    pens = SelectField('pens', validators = [DataRequired()], coerce = int)

@app.route('/choose_pen', methods = ['GET', 'POST'])
def choose_pen():
    form = Select_Movie():
    pens = models.Pen.query.all()
    form.pens.choices = [(pen.id, pen.name) for pen in pens]
    if request.method = 'POST':
        if forms.validate_on_submit():
            return redirect(url_for('pen', id = form.penname.data))
        else:
            abort(404)
            # uses a premade template. pens.html ????
    return render_template('pens.html', name = 'Select A Movie', form = form)
