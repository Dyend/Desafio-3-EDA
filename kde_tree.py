from util import euclidean_distance
from queue import PriorityQueue

class Node:
    def __init__(self, data, identificador):
        self.left_node = None
        self.right_node = None
        self.data = data
        self.identificador = identificador

class KD_Tree:

    def __init__(self,):
        self.root = None
        self.nodes_dimension = 1
        self.size = 0

    def insert_node(self, root, data, depth, identificador):
        # Si el nodo de comparacion es vacio
        if root is None:
            # Se crea un nuevo nodo
            root = Node(data, identificador)
            # Si el arbol se encuentra vacio entonces se agrega a la raiz
            if self.size == 0:
                self.root = root
                self.size +=1
            # Se retorna el nodo creado
            return root

        # Dimension de la data en la cual se va a comparar  
        dimension = depth % self.nodes_dimension

        if data[dimension] < root.data[dimension]:
            root.left_node = self.insert_node(root.left_node, data, depth + 1, identificador)
        else:
            root.right_node = self.insert_node(root.right_node, data, depth + 1, identificador)

        return root

    # inserta un nuevo nodo desde un punto en especifico y retorna la nueva raiz
    def insert(self, data, identificador):
        if self.root is None:
            self.nodes_dimension = len(data)
        return self.insert_node(self.root, data, 0, identificador)
    
    # comparacion para ver si un nodo es igual a otro comparando su data
    def are_same(self, node, data):
        largo = len(data)
        for i in range(largo):
            if node.data[i] != data[i]:
                return False
        return True

    def search_node(self, data, root, depth):

        if root is None:
            return None

        if self.are_same(root, data):
            return root
        
        current_dimension = depth % self.nodes_dimension
        if data[current_dimension] < root.data[current_dimension]:
            return self.search_node(root.left_node, data, depth + 1)
        else:
            return self.search_node(root.right, data, depth + 1)

    def add_neighbour(self, node, neighbours, required_amount, distance, nearest_neighbours_set):
        """ Esta funcion hace uso de una priority queue que evalua en orden de izquierda a derecha la tupla ingresada
            es decir que si dos objetos tienen la misma distancia se evalua el id

            el primer parametro ingresado a la priority queue es la distancia en negativo, esto con objetivo
            de tener invertida la priority queue es decir que la mayor distancia sea remplazada
        """

        if not node.identificador in nearest_neighbours_set:
            if neighbours.qsize() < 10:
                    neighbours.put((-distance, distance, node.identificador, node))
                    nearest_neighbours_set.add(node.identificador)
            else:
                # pop last the furthest node and compare
                f_distance, furthest_distance, identificador, furthest = neighbours.get()
                if distance < furthest_distance:
                    neighbours.put((-distance, distance, node.identificador, node))
                    nearest_neighbours_set.add(node.identificador)
                else:
                    neighbours.put((f_distance, furthest_distance, identificador, furthest))

    def closer_distance(self, data, p1, p2, neighbours, required_amount, nearest_neighbours_set):

        if p1 is None or self.are_same(p1, data):
            d2 = euclidean_distance(data, p2.data)
            self.add_neighbour(p2, neighbours, required_amount, d2, nearest_neighbours_set)
            return p2

        if p2 is None or self.are_same(p2, data):
            d1 = euclidean_distance(data, p1.data)
            self.add_neighbour(p1, neighbours, required_amount, d1, nearest_neighbours_set)
            return p1

        d1 = euclidean_distance(data, p1.data)
        d2 = euclidean_distance(data, p2.data)

        if d1 < d2:
            closer = p1
            distance = d1
        else:
            closer = p2
            distance = d2

        self.add_neighbour(closer, neighbours, required_amount, distance, nearest_neighbours_set)

        return closer
        

    def get_kd_tree_neighbours(self, quantity, data):
        nearest_neighbours = PriorityQueue()
        nearest_neighbours_set = set()
        self.nearest_k_neighbours(self.root, data, 0 , nearest_neighbours, quantity, nearest_neighbours_set)
        return nearest_neighbours
        
    def nearest_k_neighbours(self, root, data, depth, neighbours, required_amount, nearest_neighbours_set):

        if root is None:
            return None

        current_dimension = depth % self.nodes_dimension

        next_branch = None
        opposite_branch = None
        if data[current_dimension] < root.data[current_dimension]:
            next_branch = root.left_node
            opposite_branch = root.right_node
        else:
            next_branch = root.right_node
            opposite_branch = root.left_node

        node = self.nearest_k_neighbours(next_branch, data, depth + 1, neighbours, required_amount, nearest_neighbours_set)
        best = self.closer_distance(data, node, root, neighbours, required_amount, nearest_neighbours_set)
        if best is not None and euclidean_distance(data, best.data) > abs(data[current_dimension] - root.data[current_dimension]):
            node = self.nearest_k_neighbours(opposite_branch, data, depth + 1, neighbours, required_amount, nearest_neighbours_set)
            best = self.closer_distance(data, node, best, neighbours, required_amount, nearest_neighbours_set)

        return best
