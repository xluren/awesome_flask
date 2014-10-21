import os
class Config(object):
    DEBUG=True
    CACHE_TYPE = 'simple'
    SECRET_KEY = "d73b04b0e696b0945283defa3eee4538"
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))  
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
class MysqlConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://hello:hello@10.210.71.145:3306/sqlalchemy'
class MongoDBConfig(Config):
    MONGOALCHEMY_DATABASE="mydb"
    MONGOALCHEMY_SERVER="10.210.71.145"
    MONGOALCHEMY_PORT=8888
POST_PER_PAGE = 3 
