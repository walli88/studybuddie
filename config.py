from os import environ

class Config:
    SECRET_KEY = environ.get('SECRET_KEY') or 'beT Yu Cant gue$$ dis'
    SSL_DISABLE = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "support@studybuddie.me"
    MAIL_PASSWORD = "tuber2014"

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}