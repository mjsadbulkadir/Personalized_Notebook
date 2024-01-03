
from flask_restful import Api
from flask import Blueprint
from app.auth.controllers.admin import LoginView,LogOutView,SignUpView

auth_blueprint =Blueprint("auth",__name__,url_prefix="/auth")
api=Api(auth_blueprint)

api.add_resource(LoginView,"/login/") 
api.add_resource(SignUpView,"/signup/")
api.add_resource(LogOutView,"/logout/")
