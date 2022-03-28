from os import listdir
import pandas as pd


def extract_raw_data_from_csv(path):
    """
    Reads in a csv file and converts the devicetime column to a datetime object
    
    :param path (string): The path to the CSV file
    :return raw_data (Pandas dataframe)
    """
    raw_data = pd.read_csv(path)
    raw_data['devicetime'] = pd.to_datetime(raw_data['devicetime'], unit='s',)
    return raw_data

def extract_raw_data_batch(path):
    """
    The function extracts the raw data from the csv files in the given path
    
    :param path (string): The path to the folder containing the csv files
    :return raw_data_list (list of Pandas dataframe). Each list contains the data from one csv file.
    """
    files_list = listdir(path)
    raw_data_list = []
    for file in files_list:
        try:
            raw_data = extract_raw_data_from_csv(f"{path}\{file}")
        except:
            print(f"Invalidad csv file : {path}\{file}")
            continue
        raw_data_list.append(raw_data)              
    return raw_data_list

def clean_prepare_data(raw_data):
    # Limit high values
    retardo_limit = 500
    # info not used in this first version                                          
    raw_data.drop(['deviceid',
                 'imei',
                 'servertime',
                 'lat',
                 'lon',
                 'operador'],
                axis='columns',
                inplace=True)
    # Due a typo is present in the data
    try:
        raw_data.drop(["cellId"], axis='columns', inplace=True)
    except:
        raw_data.drop(["cellid"], axis='columns', inplace=True)
    raw_data['retardo'] = raw_data['retardo'].apply(lambda x: x if x <= retardo_limit else retardo_limit)    
    # TODO: add resample if necesary
    return raw_data

def clean_prepare_data_batch(raw_data_list):
    prep_data_list = []
    for raw_data in raw_data_list:
        prep_data = clean_prepare_data(raw_data)
        prep_data_list.append(prep_data)
    return prep_data_list

def load_csvs_from_path(path):
    files_list = listdir(path)
    raw_data_list = []
    for file in files_list:
        try:
            raw_data = extract_raw_data_from_csv(f"{path}\{file}")
            tmp_csv = clean_prepare_data(raw_data)
        except:
            print(f"Invalidad csv file : {path}\{file}")
            continue
        raw_data_list.append(tmp_csv)              
    return raw_data_list