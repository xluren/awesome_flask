from flask import Blueprint 
from app import app,db
from app.common.models import Comment
from app.common.forms  import CommentForm
from flask import render_template





admin=Blueprint("admin",__name__)

@admin.route("/")
def admin_index():
    return "hello admin index"


@admin.route("/new")
def admin_new_view():
    comment_form=CommentForm()
    if comment_form.validate_on_submit():
        comment_form.save()
        return "save successfully"
    return render_template("/admin/new.html",form=comment_form)


