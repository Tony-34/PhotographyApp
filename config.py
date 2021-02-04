import os
import cloudinary

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Config:
    '''
    General configuration parent class
    '''
    IMAGE_API_BASE_URL = 'https ://pixabay.com/api/?key={}&q={}&image_type=photo&pretty=true'
    IMAGE_API_KEY = os.environ.get('IMAGE_API_KEY')
    SECRET_KEY = 'tony'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Avamara34@localhost/photographyweb'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    cloudinary.config(
        cloud_name='tee47-galleria',
        api_key='238974632867683',
        api_secret='8PnS4Jj90lxybYd-AKUpbDPj6jQ')

    #  email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME ='tr33947@gmail.com'
    MAIL_PASSWORD ='Avamara47'


    #simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Avamara34@localhost/photographyweb'
    DEBUG = False
class TestConfig(Config):
    pass

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Avamara34@localhost/photographyweb'
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'Test': TestConfig
}