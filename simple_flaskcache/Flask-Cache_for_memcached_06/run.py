from flask import Flask
import random

# import the flask extension
from flask.ext.cache import Cache   

app = Flask(__name__)

#import config setting
app.config.from_object("config.Config")

# register the cache instance and binds it on to your app 
app.cache = Cache(app)   

@app.route("/")
@app.cache.cached(timeout=500,key_prefix="hello")  # cache this view for 30 seconds
def cached_view():
    a=random.randint(0,100)
    return str(a)

if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')
