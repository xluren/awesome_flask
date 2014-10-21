from flask import Flask
from app.common.cache import cache



app=Flask(__name__)
app.config.from_object("config")

cache.init_app(app)

from app.module_one.views import module_one
from app.module_two.views import module_two
from app.module_three.views import module_three

app.register_blueprint(module_one,url_prefix="/module_one")
app.register_blueprint(module_two,url_prefix="/module_two")
app.register_blueprint(module_three,url_prefix="/module_three")


