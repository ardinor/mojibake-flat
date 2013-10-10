from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index=True)
    path = db.Column(db.String(240), index=True)
    date = db.Column(db.DateTime)
    categories = db.Column(db.String(120))

    def __repr__(self):
        return '<Post %r>' % (self.title)
