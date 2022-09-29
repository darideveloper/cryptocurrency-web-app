from flask import Blueprint, request
from utils import database

# Create blueprin
blueprint_api = Blueprint ('api', __name__)

# api endpoint in get
@blueprint_api.route ("/", methods=["GET"])
def query ():
    """ return query data from csv files  """
    
    # read query variables
    name = request.args.get("name")
    date = request.args.get("date")
    
    # Get data from csv files
    data = database.get_data ()
    
    # Filter required data
    
    # Show data
    return {
        "name": name,
        "date": date,
        "data": data
    }
    