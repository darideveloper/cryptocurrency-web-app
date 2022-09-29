from utils import database
from flask import Blueprint, request
from datetime import datetime

def filter_data (data:list, start_date:str, end_date:str, name:str):
    
    data_filtered = []
    for row in data:
        
        # Get row date
        date_text = row[3]
        date = datetime.strptime(date_text, "%Y-%m-%d")
        
        # Converr start date to filter
        if not start_date:
            start_date = datetime(1999, 1, 1)
            
        # Converr end date to filter
        if not end_date:
            end_date = datetime.now ()      
            
        if start_date <= date <= end_date:
            data_filtered.append (row)
    
    return data_filtered
    

# Create blueprin
blueprint_api = Blueprint ('api', __name__)

# api endpoint in get
@blueprint_api.route ("/", methods=["POST"])
def query ():
    """ return query data from csv files  """
    
    # read query variables from json
    json_data = request.json

    name = json_data["name"]
    start_date = json_data["start_date"]
    end_date = json_data["end_date"]
    
    # Get data from csv files
    data = database.get_data ()
    
    # Filter data with function
    data_filtered = filter_data (data, start_date, end_date, "")
    
    # Show data filtered
    return {
        "name": name,
        "data": data_filtered,
    }
    