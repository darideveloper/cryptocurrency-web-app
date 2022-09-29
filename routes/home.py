from flask import Blueprint, request, render_template

# Create blueprin
blueprint_home = Blueprint ('home', __name__)

@blueprint_home.route ("/")
def index ():
    return render_template ("index.html", current_page="home")