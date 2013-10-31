from app import db

category_post = db.Table('category_post',
                         db.Column('category_id',
                            db.Integer,
                            db.ForeignKey('category.id')),
                         db.Column('post_id',
                            db.Integer,
                            db.ForeignKey('post.id')))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index=True)
    path = db.Column(db.String(240), index=True)
    date = db.Column(db.DateTime)
    categories = db.Column(db.String(120))
    categories = db.relationship('Categories', secondary=category_post,
                                 backref=db.backref('categories',
                                                    lazy='dynamic'))

    def __repr__(self):
        return '<Post {}>'.format(self.title)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    posts = db.relationship('Posts', secondary=category_post,
                            backref=db.backref('posts', lazy='dynamic'))

    def __repr__(self):
        return '<Category {}}>'.format(self.name)
