from  flask_wtf import Form
from  wtforms   import TextField,TextAreaField
from  wtforms.validators   import DataRequired,ValidationError


from  app import db
from  app.common.models import Comment

class CommentForm(Form):
    table_class = Comment
    comment=TextAreaField('comment', 
                        validators=[DataRequired()])
    email=TextField('email',
                        validators=[DataRequired()])
    username=TextField("username",
                        validators=[DataRequired()])
    ur_url=TextField('ur_url',
                        validators=[DataRequired()])
    instance=None

    def __init__(self,table=None,*args, **kwargs):
        if table is not None:
            self.instance=table
            self._copy_data_to_form()

    def _copy_data_to_form(self):
        self.comment.data = self.instance.comment
        self.email.data   = self.instance.email
        self.username.data= self.instance.username
        self.ur_url.data  = self.instance.ur_url

    def save(self):
        if self.instance  is None:
            self.instance=self.table_class()
        self.instance.comment=self.comment.data
        self.instance.email=self.email.data
        self.instance.username=self.username.data
        self.instance.ur_url=self.ur_url.data
        db.session.add(self.instance)
        db.session.commit()
