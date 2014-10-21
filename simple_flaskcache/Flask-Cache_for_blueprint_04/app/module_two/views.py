from flask import Blueprint
import time,random

from app.common.cache import cache

module_two=Blueprint("module_two",__name__)

def get_number():
    a=random.randint(0,100)
    return str(a)

def get_time():
    return time.ctime()


@module_two.route("/")
@cache.cached(timeout=10)
def module_two_index():
    return """<lu>
            <li>the datetime is {datetime}</li>
            <li>the random number is {random_number}</li>
              </lu>""".format(datetime=get_time(),random_number=get_number())


