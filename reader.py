from csv import reader

def read_file(file_name):
    with open(file_name, 'r') as read_obj:
        return list(reader(read_obj))