from flask import Flask
import logging
from logging.handlers import RotatingFileHandler



app = Flask(__name__)
app.config.from_object("config")

'''register_blueprint'''
from app.module_one.views import module_one
from app.module_two.views import module_two
app.register_blueprint(module_one, url_prefix='/module_one')
app.register_blueprint(module_two, url_prefix='/module_two')
print app.url_map

'''use logging'''
handler = RotatingFileHandler('foo_bar.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

