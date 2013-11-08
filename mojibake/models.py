from app import db

tags = db.Table('tags',
                 db.Column('post_id',
                    db.Integer,
                    db.ForeignKey('post.id')),
                 db.Column('tag_id',
                    db.Integer,
                    db.ForeignKey('tag.id')))

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    posts = db.relationship('Post', backref='category',
                                lazy='dynamic')

    def __repr__(self):
        return '<Category {}>'.format(self.name)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index=True)
    path = db.Column(db.String(240), index=True)
    date = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    tags = db.relationship('Tag', secondary=tags,
                                 backref=db.backref('posts',
                                                    lazy='dynamic'))

    def __repr__(self):
        return '<Post {}>'.format(self.title)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return '<Tag {}>'.format(self.name)


