# Desafio-3-EDA

# Problema a solucionar

Se pide encontrar, dentro de un dataset de 1800 autos, los 10 autos que mas similitudes tengan con un auto que se seleccione como referencia. Se deben implementar 3 tipos de busquedas: ingresar la id de un auto para mostrar su información, ingresar la id de un auto para encontrar los 10 mas parecidos en caracteristicas y finalmente ingresar cada una de las caracteristicas del auto para encontrar los 10 autos que más se parezcan en lo ingresado.

# Solución implementada

Para poder lograr lo anterior utilizamos el KD-Tree, el cual es una estructura de datos espacial que permitirá, mediante la busqueda por distancia entre vectores n dimensionales, encontrar los nodos que presenten una distancia euclidiana menor, respecto de un vector predeterminado. Para esta solución además se utilizará una cola con prioridad, la cual permitira ir guardando los 10 nodos que más se parezcan al nodo (o vector) que se este utilizando (o menor distancia euclidiana tengan entre si), que para este caso sera el auto con sus caracteristicas ( vector con números que representan sus caracteristicas, transformados mediante one hot enconding desde el dataset).

