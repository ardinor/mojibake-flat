from app import db

category_post = db.Table('category_post',
                         db.Column('post_id',
                            db.Integer,
                            db.ForeignKey('Post.id')),
                         db.Column('category_id',
                            db.Integer,
                            db.ForeignKey('Category.id')))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index=True)
    path = db.Column(db.String(240), index=True)
    date = db.Column(db.DateTime)
    #categories = db.Column(db.String(120))
    categories = db.relationship('Category', secondary=category_post,
                                 backref=db.backref('Post',
                                                    lazy='dynamic'))

    def __repr__(self):
        return '<Post {}>'.format(self.title)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return '<Category {}}>'.format(self.name)
