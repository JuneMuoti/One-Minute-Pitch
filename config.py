import os
class Config:

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
    
