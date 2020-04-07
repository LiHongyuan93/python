import logging
import os
from logging.config import fileConfig

from flask import Flask
from flask_login import LoginManager

from conf.config import config

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.go_login'
fileConfig('conf/log-app.conf')

def get_logger(name):
    return logging.getLogger(name)


def get_basedir():
    return os.path.abspath(os.path.dirname(__file__))


def get_config():
    return config[os.getenv('FLASK_CONFIG') or 'default']


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    login_manager.init_app(app)

    from app.api.AdminController import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    from app.api.AuthController import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
