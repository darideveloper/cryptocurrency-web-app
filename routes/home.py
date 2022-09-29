from flask import Blueprint, request

# Create blueprin
blueprint_home = Blueprint ('home', __name__)

@blueprint_home.route ("/")
def index ():
    return "Home"