import reader
import kde_tree
import sys
import util

DATA = 'data/car.data'
ATTRIBUTES = 'data/attributes.json' 

if __name__ == "__main__":
    cars = reader.read_data_set(DATA)
    attributes = reader.read_attributes(ATTRIBUTES)
    encoded_car_list = util.encode_data_set(cars, attributes)

    print('Finalizado')