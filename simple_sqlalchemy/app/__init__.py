from flask import Flask
from flask.ext.sqlalchemy  import SQLAlchemy


app=Flask(__name__)
app.config.from_object('config.TestConfig')
db=SQLAlchemy(app)


from app.admin.views import admin
app.register_blueprint(admin,url_prefix="/admin")


db.create_all()
