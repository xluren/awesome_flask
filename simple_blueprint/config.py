DEBUG = True

import os,sys
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
#DATABASE_CONNECT_OPTIONS = {}
CSRF_ENABLED     = True
CSRF_SESSION_KEY = "secret"
SECRET_KEY = "secret"
LOG_PATH=sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"/log")))
