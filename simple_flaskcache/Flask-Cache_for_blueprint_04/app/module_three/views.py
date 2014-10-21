from flask import Blueprint 
import random,time

from app.common.cache import cache

module_three=Blueprint("module_three",__name__)


@cache.cached(timeout=50,key_prefix="hello")
def get_number():
    a=random.randint(0,100)
    return str(a)

def get_time():
    return time.ctime()

@module_three.route("/")
def module_one_index():
    return """<lu>
            <li>datetime is :{datetime}</li>
            <li>random number is:{random_number}</li>
            </lu>""".format(datetime=get_time(),random_number=get_number())

