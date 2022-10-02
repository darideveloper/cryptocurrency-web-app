from flask import Flask
from routes.api import blueprint_api
from routes.home import blueprint_home

app = Flask (__name__)

# Register blueprints
app.register_blueprint (blueprint_home, url_prefix="/")
app.register_blueprint (blueprint_api, url_prefix="/api")