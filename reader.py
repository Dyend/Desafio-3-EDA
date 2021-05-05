from csv import reader
import json
def read_data_set(file_name):
    with open(file_name, 'r') as read_obj:
        return list(reader(read_obj))

def read_attributes(file_name):
    with open(file_name) as json_file:
        return json.load(json_file)