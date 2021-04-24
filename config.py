import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'H4dj046N1D4R$'