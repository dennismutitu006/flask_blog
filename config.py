import os

basedir = os.path.abspath(os.path.dirname(__file__))
# /home/oleg/Desktop/flsk_blog/app/config.py

class Config:
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
