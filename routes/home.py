from flask import Blueprint, request, render_template

# Create blueprin
blueprint_home = Blueprint ('home', __name__)

@blueprint_home.route ("/")
def index ():
    return render_template ("index.html", current_page="home", base_path="./")

@blueprint_home.route ("/search/")
def search_all ():
    return render_template ("search.html", current_page="all", base_path="../")