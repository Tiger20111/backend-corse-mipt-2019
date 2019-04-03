import os

class Config(object):
    # main config
    SECRET_KEY = 'my_precious'
    SECURITY_PASSWORD_SALT = 'my_precious_two'
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    # mail settings
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    # mail accounts
    MAIL_DEFAULT_SENDER = 'dimka.nevstruev@bk.ru'
    MAIL_USERNAME = 'dimka.nevstruev@bk.ru'
    MAIL_PASSWORD = '321ewq'