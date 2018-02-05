import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://june:1234@localhost/pitch'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    #general configuration parent class
    pass

class ProdConfig(Config):
    #production cpnfiguration child class

    pass


class DevConfig(Config):

    #Development configuration child class

    DEBUG = True

config_options ={
'development':DevConfig,
'production':ProdConfig
    }
    
