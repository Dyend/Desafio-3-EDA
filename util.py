
import numpy as np

def normal_encoding(attributes):
    """Dict with binary encoded vector"""
    encoded_attributes = dict()
    for index, attr in enumerate(attributes):
        attr = attr.replace('-', '')
        encoded_attributes[attr] = str(index)
    show_encoding(encoded_attributes)
    return encoded_attributes


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
    new_car = []
    
    for index, attr in enumerate(car):
        # Replace car attribute in index position with attribute encoded
        #car[index] = attributes[index][attr]
        for a in attributes[index][attr]:
            new_car.append(int(a))
    return np.asarray(new_car)
    
def encode_data_set(cars, attributes_encoded):

    encoded_car_list = []
    for car in cars:
        """ remove acceptability attr (last attr)"""
        car.pop()
        encoded_car = encode_car(attributes_encoded, car)
        #input()
        encoded_car_list.append(encoded_car)
    return encoded_car_list


def print_car(identificador, car):
    print('id: ', identificador)
    print('buying: ', car[0])
    print('maint: ', car[1])
    print('doors: ', car[2])
    print('persons: ', car[3])
    print('lug_boot: ', car[4])
    print('safety: ', car[5])

def print_vecinos(vecinos, cars):
    print('Se encontraron : ', vecinos.qsize(), ' vecinos')
    while not vecinos.empty():
        distance, identificador, vecino = vecinos.get()
        print('Distancia :', distance)
        print_car(identificador, cars[identificador])

    input('Enter para continuar')

def euclidean_distance(vector1, vector2):
    return np.sqrt(np.sum((vector1 - vector2)**2))