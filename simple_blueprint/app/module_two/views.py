from flask import Blueprint, render_template,url_for,redirect,session

module_two = Blueprint('module_two', __name__)

@module_two.route('/')
def index():
    return render_template('/module_two/index.html')

@module_two.route('/session')
def session_test():
    if session.get("hello"):
        return "this is session[hello] show it "
    return "no session in session"
@module_two.route('/popsession')
def pop_session():
    if session.get('hello'):
        session.pop('hello',None)
        return "session had poped"
    return "this  is no session in session"
