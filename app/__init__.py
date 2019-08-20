from flask import Flask
from config import Config
#import pdb;pdb.set_trace()
app = Flask(__name__)
'''
for i in dir(app):
    print(i)
'''
app.config.from_object(Config)
from app import routes
