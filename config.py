
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/database'
    SQLALCHEMY_TRACK_MODIFICATIONS = False