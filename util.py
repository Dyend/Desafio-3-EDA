
import numpy as np


def one_hot_encoding(attributes):
    """Dict with binary encoded vector"""
    encoded_attributes = dict()
    zeros = len(attributes)
    base = '0' * zeros
    print('base ', base)
    for index, attr in enumerate(attributes):
        # replace 0 with 1 in index position
        binary = base[index + 1:] + '1' + base[:index]
        # Remove - from key because on dataset is not with -
        attr = attr.replace('-', '')
        encoded_attributes[attr] = binary
    show_encoding(encoded_attributes)
    return encoded_attributes


def show_encoding(encoding_dict):
    for key, value in encoding_dict.items():
        print(key, ':', value)
    print('--------')

""" 
    attributes is a list with dictionaries
""" 
def encode_car(attributes, car):
    for index, attr in enumerate(car):
        # Replace car attribute in index position with attribute encoded
        car[index] = attributes[index][attr]
    """ remove acceptability attr"""
    car.pop()
    return np.asarray(car)
    
def encode_data_set(cars, attributes):
    buying_categories = one_hot_encoding(attributes['buying'])
    maint = one_hot_encoding(attributes['maint'])
    doors_categories = one_hot_encoding(attributes['doors'])
    persons_categories = one_hot_encoding(attributes['persons'])
    lug_boot_categories = one_hot_encoding(attributes['lug_boot'])
    safety_categories = one_hot_encoding(attributes['safety'])
    acceptability_categories = one_hot_encoding(attributes['acceptability'])
    attributes_encoded = [buying_categories, maint, doors_categories,
                          persons_categories, lug_boot_categories, safety_categories, acceptability_categories]
    encoded_car_list = []
    for car in cars:
        print('car ', car)
        # attr order buying, maint, doors, persons, lug_boot, safety
        encoded_car = encode_car(attributes_encoded, car)
        print('encoded car ', encoded_car)
        encoded_car_list.append(encoded_car)
    return encoded_car_list
