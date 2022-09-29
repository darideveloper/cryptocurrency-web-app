from flask import Blueprint, request, render_template

# Create blueprin
blueprint_home = Blueprint ('home', __name__)

@blueprint_home.route ("/")
def index ():
    # Render home template
    return render_template ("index.html", current_page="home")

@blueprint_home.route ("/search/")
def search_all ():
    data = []
    show = {
        "name": True,
        "symbol": True,
        "date": True,
        "high": True,
        "low": True,
        "open": True,
        "close": True,
        "volume": True,
        "marketcap": True,
    }
    
    # Return search all template
    return render_template ("search.html", current_page="all", show=show, data=data)