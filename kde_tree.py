
class Node:
    def __init__(self, data):
        self.left_node = None
        self.right_node = None
        self.data = data

class KD_Tree:

    def __init__(self,):
        self.root = None
        self.nodes_dimension = 1
        self.size = 0

    def insert_node(self, root, data, depth):
        # Si el nodo de comparacion es vacio
        if root is None:
            # Se crea un nuevo nodo
            root = Node(data)
            # Si el arbol se encuentra vacio entonces se agrega a la raiz
            if self.size == 0:
                self.root = root
                self.size +=1
            # Se retorna el nodo creado
            return root

        # Dimension de la data en la cual se va a comparar  
        dimension = depth % self.nodes_dimension

        if data[dimension] < root.data[dimension]:
            root.left_node = self.insert_node(root.left_node, data, depth + 1)
        else:
            root.right_node = self.insert_node(root.right_node, data, depth + 1)

        return root

    # inserta un nuevo nodo desde un punto en especifico y retorna la nueva raiz
    def insert(self, root, data):
        return self.insert_node(root, data, 0)
    
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

    def search(self, data, root = None):
        if root is None:
            root = self.root
        return self.search_node(data, root, 0)
    