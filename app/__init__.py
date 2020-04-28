from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstarp = Bootstrap()

#initializing application
def create_app(config_name):
    app = Flask(__name__)

    #create the app configurations
    app.config.from_object(config_options[config_name])


#Setting up Configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')


from app import views