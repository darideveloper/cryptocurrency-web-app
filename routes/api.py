from flask import Blueprint, request
from utils import database

# Create blueprin
blueprint_api = Blueprint ('api', __name__)

# api endpoint in get
@blueprint_api.route ("/", methods=["GET"])
def query ():
    """ return query data from csv files  """
    
    # read query variables from json
    json_data = request.json
    name = json_data["name"]
    start_date = json_data["start_date"]
    end_date = json_data["end_date"]
    
    # Get data from csv files
    data = database.get_data ()
    
    # Filter required data
    
    # Show data
    return {
        "name": name,
        "start_date": start_date,
        "end_date": end_date
    }
    