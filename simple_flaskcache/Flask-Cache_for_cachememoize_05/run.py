import time
from flask.ext.cache import Cache
from flask import Flask

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
app.cache = Cache(app)

@app.cache.cached(timeout=50)
def get_current_time_and_name(name):
    return "%s - %s\n" % (name, time.ctime())

@app.route("/<name>")
def view(name):
    return get_current_time_and_name(name)

@app.cache.memoize(timeout=50)
def get_current_time_and_name_memoize(name):
    return "%s - %s\n" % (name, time.ctime())

@app.route("/hello/<name>")
def memoize_view(name):
    return get_current_time_and_name_memoize(name)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
