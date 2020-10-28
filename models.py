from main import db


# pen tag joining table
PenTag = db.Table('PenTag', db.Model.metadata,
db.Column('pid', db.Integer, db.ForeignKey('Pen.id')),
db.Column('tid', db.Integer, db.ForeignKey('Tag.id'))
)


# brands
class Brand(db.Model):
    __tablename__ = 'Brand'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    desc = db.Column(db.Text)
    photo = db.Column(db.Text)
    deletable = db.Column(db.Boolean)
    pens = db.relationship('Pen', backref='brand')

    def __str__(self):
        return self.name


# credits to information or images used in the website
class Credit(db.Model):
    __tablename__ = "Credit"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    link = db.Column(db.Text, nullable = False)

    def __str__(self):
        return self.name


# pens
class Pen(db.Model):
    __tablename__ = "Pen"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    desc = db.Column(db.Text)
    photo = db.Column(db.Text)
    bid = db.Column(db.Integer,db.ForeignKey('Brand.id'), nullable = False)
    tags = db.relationship('Tag', secondary=PenTag, back_populates='pens')


    def __str__(self):
        return self.name


# tags
class Tag(db.Model):
    __tablename__ = "Tag"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    desc = db.Column(db.Text)
    photo = db.Column(db.Text)
    pens = db.relationship('Pen', secondary=PenTag, back_populates='tags')

    def __str__(self):
        return self.name