from main import db

# pen brands
class Brand(db.Model):
    __tablename__ = 'Brand'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    desc = db.Column(db.Text)
    photo = db.Column(db.Text)
    pens = db.relationship('Pen', backref='brand')

    def __str__(self):
        return self.name

# credits to information or images used in the website
class Credits(db.Model):
    __tablename__ = "Credits"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    link = db.Column(db.Text, nullable = False)

    def __str__(self):
        return self.name

# individual pens
class Pen(db.Model):
    __tablename__ = "Pen"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    desc = db.Column(db.Text)
    photo = db.Column(db.Text)
    bid = db.Column(db.Integer,db.ForeignKey('Brand.id'), nullable = False)
    tags = db.relationship('PenTags', back_populates='pen')

    def __str__(self):
        return self.name

# pen tags
class Tag(db.Model):
    __tablename__ = "Tag"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    desc = db.Column(db.Text)
    photo = db.Column(db.Text)
    pens = db.relationship('PenTags', back_populates='tag')

    def __str__(self):
        return self.name

# pen tag joining table
class PenTags(db.Model):
    __tablename__ = "PenTags"

    id = db.Column(db.Integer, primary_key = True)
    pid = db.Column(db.Integer, db.ForeignKey('Pen.id'))
    tid = db.Column(db.Integer, db.ForeignKey('Tag.id'))
    pen = db.relationship('Pen', back_populates='tags')
    tag = db.relationship('Tag', back_populates='pens')

    def __str__(self):
        return self.name
