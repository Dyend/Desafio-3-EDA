import reader
from kde_tree import KD_Tree
import sys
import util
import os
from queue import PriorityQueue

DATA = 'data/car.data'
ATTRIBUTES = 'data/attributes.json' 

def print_options():
    print('Seleccione una de las opciones disponibles.')
    print('a.- Mostrar información de un auto específico (id)).')
    print('b.- Mostrar información de los 10 autos más parecidos dada un (id).')
    print('c.- Mostrar información de los 10 autos más parecidos segun vector de atributos.')
    print('Enter para salir.')


def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

def select_car(cars):
    print('Especifique id del auto')
    id_auto = None
    while id_auto is None:
        try:
            id_auto = int(input())
        except:
            pass
    return id_auto



def a(cars):
    id_auto = select_car(cars)
    util.print_car(id_auto, cars[id_auto])

def b(kd_tree, cars, attributes_encoded):
    id_auto = select_car(cars)
    util.print_car(id_auto, cars[id_auto])
    input('Presione enter para continuar.')
    screen_clear()
    data = util.encode_car(attributes_encoded, cars[id_auto])
    nearest_neighbours = kd_tree.get_kd_tree_neighbours(10, data)
    util.print_vecinos(nearest_neighbours, cars)

def c(kd_tree, attributes_encoded, attributes):
    """ lista con los atributos a buscar"""
    data = []
    for index, key in enumerate(attributes):
        length_attributes = len(attributes_encoded[index])
        selected_attr_index = None
        while selected_attr_index is None or not (selected_attr_index >= 0 and selected_attr_index < length_attributes):
            screen_clear()
            print('Seleccione un atributo de ' + key)
            for sub_index, attr in enumerate(attributes_encoded[index]):
                print(sub_index, '- ', attr)
            try:
                selected_attr_index = int(input())
                attribute = attr
            except:
                pass
        data.append(int(attributes_encoded[index][attribute]))
    nearest_neighbours = kd_tree.get_kd_tree_neighbours(10, data)
    util.print_vecinos(nearest_neighbours, cars)

def options(kd_tree, cars, attributes_encoded, attributes):
    while True:
        print_options()
        opcion = input()
        #screen_clear()
        if opcion == 'a':
            a(cars)
        elif opcion == 'b':
            b(kd_tree, cars, attributes_encoded)
        elif opcion == 'c':
            c(kd_tree, attributes_encoded, attributes)
        else:
            sys.exit(-1)




if __name__ == "__main__":
    cars = reader.read_data_set(DATA)
    attributes = reader.read_attributes(ATTRIBUTES)
    """ Remove acceptability_categories"""
    attributes.pop('acceptability')
    #acceptability_categories = util.one_hot_encoding(attributes['acceptability'])
    buying_categories = util.normal_encoding(attributes['buying'])
    maint = util.normal_encoding(attributes['maint'])
    doors_categories = util.normal_encoding(attributes['doors'])
    persons_categories = util.normal_encoding(attributes['persons'])
    lug_boot_categories = util.normal_encoding(attributes['lug_boot'])
    safety_categories = util.normal_encoding(attributes['safety'])

    attributes_encoded = [buying_categories, maint, doors_categories,
                          persons_categories, lug_boot_categories, safety_categories]#, acceptability_categories]

    encoded_car_list = util.encode_data_set(cars, attributes_encoded)
    kd_tree = KD_Tree()
    for index, data in enumerate(encoded_car_list):
        kd_tree.insert(data, index)
    print('Datos cargados')
    options(kd_tree, cars, attributes_encoded, attributes)
