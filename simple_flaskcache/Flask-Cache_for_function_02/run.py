from flask  import Flask
from flask.ext.cache import Cache
import random,time



app=Flask(__name__)
app.config.from_object("config.Config")
app.cache=Cache(app)


@app.cache.cached(timeout=10,key_prefix="hello")
def get_number():
    s=random.randint(0,100)
    return str(s)

'''
    @app.cache.cached(timeout=10,key_prefix="hello")
    add or remove the  deractor to see the function of  key_prefix
'''
def get_datetime():
    return time.ctime()

@app.route("/")
def main_index():
    return """<lu>
            <li>the datetime is {datetime}</li>
            <li>the number is {random_number}</li>
            </lu>""".format(
                datetime=get_datetime(),
                random_number=get_number()
            )

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
