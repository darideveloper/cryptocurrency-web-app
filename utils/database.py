import os
import csv

def get_data ():
    """ get data from local csv files, for simlate database

    Returns:
        list: nested list of coins history, with the columns:
            SNo,Name,Symbol,Date,High,Low,Open,Close,Volume,Marketcap
    """
    
    data = []
    
    # Get csv files in data folder
    current_folder = os.path.dirname(__file__)
    data_folder = os.path.join (current_folder, "data")
    csv_files = os.listdir (data_folder)
    
    # Loop for each csv file
    for csv_file in csv_files:
        
        # File path
        csv_file_path = os.path.join (data_folder, csv_file)
        
        # Read file content
        with open (csv_file_path) as file:
            csv_rows = list(csv.reader (file))
            
        # ignore header from rows
        csv_rows = csv_rows[1:]
        
        # Save csv rows in general data variable
        data += csv_rows
    
    return data