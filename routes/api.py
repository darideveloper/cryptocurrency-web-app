from utils import database
from flask import Blueprint, request
from datetime import datetime

def filter_data (data:list, start_date_text:str, end_date_text:str, coin:str):
    
    data_filtered = []
    for row in data:
        
        # Filter by coin
        if coin:
            coin_row = row[1].lower()
            
            # Skip current row if coint dont match
            if coin_row != coin:
                continue
        
        # Get row date
        date_row = row[3]
        date = datetime.strptime(date_row, "%Y-%m-%d")
        
        # Converr start date to filter
        if start_date_text:
            start_date = datetime.strptime(start_date_text, "%Y-%m-%d")
        else:
            start_date = datetime(1999, 1, 1)
            
        # Converr end date to filter
        if end_date_text:
            end_date = datetime.strptime(end_date_text, "%Y-%m-%d")
        else:
            end_date = datetime.now ()      
            
        # Filter with dates
        if start_date <= date <= end_date:
            data_filtered.append (row)
            
            
    
    return data_filtered
    

# Create blueprin
blueprint_api = Blueprint ('api', __name__)

# api endpoint in get
@blueprint_api.route ("/", methods=["POST"])
def query_all ():
    
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

# api endpoint in get
@blueprint_api.route ("/<coin>", methods=["POST"])
def query_coin (coin):
    
    # read query variables from json
    json_data = request.json

    name = json_data["name"]
    start_date = json_data["start_date"]
    end_date = json_data["end_date"]
    
    # Get data from csv files
    data = database.get_data ()
    
    # Filter data with function
    data_filtered = filter_data (data, start_date, end_date, coin)
    
    # Show data filtered
    return {
        "name": name,
        "data": data_filtered,
    }
    