from flask_restful import Api
from flask import Blueprint
from app.auth.controllers.admin import LoginView, SignUpView
from app.md.controllers.note import NoteView

md_blueprint = Blueprint("md", __name__, url_prefix="/md")

api = Api(md_blueprint)

api.add_resource(NoteView, "/note/")  
