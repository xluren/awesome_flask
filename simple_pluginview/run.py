from flask import Flask, render_template, abort,request, redirect, url_for, flash,session
from flask.views import View, MethodView
import os

SECRET_KEY = 'some_secret_key'
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)  


'''basic principle'''
@app.route("/basic")
def basic_view():
    return "this is a basic principle"

'''two kinds of pluginview'''
'''
    demo one:
    we use View & dispatch 
'''
class demo_one(View):
    def dispatch_request(self):
        return "Hello demo one!"

''' demo two :
    we use MethodView(Method just like get put ...)
    also include sone method like get ,put ....
'''

class demo_two(MethodView):
    def get(self):
        return "hello demo two this  is get  method"

    def post(self):
        return "hello demo two this is put method"
'''
    demo three from http://flask.pocoo.org/
'''
class ListView(View):
    def get_template_name(self):
        raise NotImplementedError()
    def render_template(self, str):
        return "this is  father class template"+str
    def dispatch_request(self):
        str=self.get_objects()
        new_str=self.render_template(str)
        return new_str

class UserView(ListView):

    def get_template_name(self):
        return 'hello world'

    def get_objects(self):
        return "hello"

''' demo foue :
    we use MethodView(Method just like get put ...)
    also include sone method like get ,put ....
    but we hide Method 
'''

class demo_four(MethodView):
    methods = ['GET', 'POST']
    def dispatch_request(self):
        if request.method=="GET":
            return "this demo four with GET method"
        else:
            return "this demo four with other methos" 
''' 
    demo five :
        this demo will be used in project frequently
'''
class demo_five(View):
    def dispatch_request(self):
        return render_template(self.template)
    def __init__(self,template):
        self.template=template

'''
    demo six:
        this is a  demo which includes  decorator
    it includes three parts
        one     : login to set  session
        two     : decoratoe to check session
        three   : a  view which use decorator
'''

class login(View):
    def dispatch_request(self):
        session["hello"]=True
        return "you have log in with hello"


def user_required(f):
    """Checks whether user is logged in or raises error 401."""
    def decorator(*args, **kwargs):
        if not session.get("hello"):
            abort(401)
        return f(*args, **kwargs)
    return decorator

class demo_six(View):
    decorators = [user_required]
    def __init__(self,template):
        self.template=template
    def dispatch_request(self):
        return render_template(self.template)

        
'''add url to route '''        
app.add_url_rule('/demo_one', view_func=demo_one.as_view('demo_one'))
app.add_url_rule('/demo_two', view_func=demo_two.as_view('demo_two'), methods=['GET', 'POST']) 
app.add_url_rule('/demo_three', view_func=UserView.as_view('demo_three')) 
app.add_url_rule('/demo_four', view_func=demo_four.as_view('demo_four')) 
app.add_url_rule('/demo_five', view_func=demo_five.as_view('demo_five',template="demo_five.html")) 
app.add_url_rule('/login',view_func=login.as_view('login'))
app.add_url_rule('/demo_six',view_func=demo_six.as_view('demo_six',template='demo_six.html'))


if __name__ == "__main__":
    app.run(host="10.210.71.145")
