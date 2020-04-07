from flask import Blueprint
admin = Blueprint('admin', __name__)
from app.api import AdminController
auth = Blueprint('auth', __name__)
from app.api import AuthController