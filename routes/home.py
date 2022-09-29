from flask import Blueprint, request, render_template

# Create blueprin
blueprint_home = Blueprint ('home', __name__)

@blueprint_home.route ("/")
def index ():
    # Render home template
    return render_template ("index.html", current_page="home")

@blueprint_home.route ("/search/")
def search_all ():   
    # Return search all template
    return render_template ("search.html", current_page="all")

@blueprint_home.route ("/search/<coin>")
def search_coin (coin):   
    # Return search all template
    return render_template ("search.html", current_page=coin)