import os

class Config:

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    QUOTES_API = 'http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY = 'jacky2'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mukamisha:mukamisha@97@localhost/blogs'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mukamisha:mukamisha@97@localhost/pitch_test'
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mukamisha:mukamisha@97@localhost/blogs'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig

}




