from flask import Flask
from werkzeug.routing import BaseConverter
class RegexConverter(BaseConverter):
    def __init__(self, map, *args):
        print map
        self.map = map
        self.regex = args[0]

app = Flask(__name__)
app.url_map.converters['regex'] = RegexConverter



@app.route('/<regex(".*hello"):hello>')
def deal_hello(hello):
    return hello

@app.route('/<regex("[abcABC0-9]{4,6}"):uid>-<slug>/')
def example(uid, slug):
    '''
        url:/aaaa-hello
        return : uid:aaa,slug:hello
    '''
    return "uid: %s, slug: %s" % (uid, slug)


@app.route('/view/<regex("[a-zA-Z0-9]+"):uuid>/')
def view(uuid):
    """
    url: /view/1010000000125259/
    result: view uuid:1010000000125259
    """
    return "view uuid: %s" % (uuid)

@app.route('/<regex(".*"):url>')
def not_found(url):
    """
    url: /hello
    result: not found: 'hello'
    """
    return "not found: '%s'" % (url)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
