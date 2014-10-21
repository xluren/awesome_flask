from flask import Flask
from flask.ext.cache import Cache
from views import main_index
from views import get_number

app = Flask(__name__)
app.config.from_object("config.Config")
app.cache = Cache(app)


app.cache.cached(timeout=10)(get_number)
app.add_url_rule("/", view_func=main_index)
