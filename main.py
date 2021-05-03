import reader
import kde_tree
import sys

FILE_NAME = 'data/car.data'

if __name__ == "__main__":
    cars = reader.read_file(FILE_NAME)
    for car in cars:
        print(car)
        input()
    print('Finalizado')