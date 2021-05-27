from flask import Flask
from .backend.views import register_call_views

app = Flask(__name__)
register_call_views(app)