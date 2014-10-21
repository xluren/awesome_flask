from flask import Blueprint, render_template,url_for,redirect,session
from app import app
from flask.views import View, MethodView


module_one= Blueprint('module_one', __name__)

@module_one.route('/')
def index():

    '''
        test usage of session 
        use  session.get[key] to get the value
        use  session[key]=value to set session
        use  session.pop(key, None) to deal
    '''

    if session.get('hello'):
        return redirect(url_for("module_one.redirect_mod_two"))
    session["hello"]=True
    return render_template('module_one/index.html')


'''
    in this  function  just to test the  redirect in 
    Blueprint. when we want wo redirect from Blueprint
    module_one to module_two,we should use 
    url_for("module_two.function")
'''

@module_one.route('/redirect')
def redirect_mod_two():

    '''test the usage of logging'''
    app.logger.error("hello flask logger error test")
    app.logger.warning("hello flask logger warning test")
    app.logger.info('i will jump to %s' % url_for("module_two.index"))
    return redirect(url_for("module_two.index"))

class admin_plug_one(View):
    def dispatch_request(self):
        return "this is admin plugable view demo one "

class admin_plug_two(MethodView):
    def get(self):
        return "this is  admin plugable  demo two with Method of GET"

    def post(self):
        return "this  is  admin plugable demo two  with Method of POST"

module_one.add_url_rule('/admin_plug_one', view_func=admin_plug_one.as_view('admin_plug_one'))
module_one.add_url_rule('/admin_plug_two', view_func=admin_plug_two.as_view('admin_plug_two'), methods=['GET', 'POST']) 



