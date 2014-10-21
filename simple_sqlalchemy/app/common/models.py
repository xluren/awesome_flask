from app import db


class Comment(db.Model):
    __tablename__="comments"
    id          = db.Column(db.Integer,primary_key=True)
    comment     = db.Column(db.Text,nullable=False,default=u'hello world')
    email       = db.Column(db.String,nullable=False,default=u'Untitled')
    username    = db.Column(db.String,nullable=False,default=u'anoymous')
    ur_url      = db.Column(db.String,nullable=False,default=u'#')

    def __init__(self,comment="hello world",email="untitiled",username="anoymous",ur_url="#"):
        self.comment    = comment
        self.email      = email
        self.username   = username
        self.ur_url     = ur_url

    def __repr__(self):
        return "<commects %r>" % self.email
