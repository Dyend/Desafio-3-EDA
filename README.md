# Desafio-3-EDA

# Problema a solucionar

Se pide encontrar, dentro de un dataset de 1800 autos, los 10 autos que mas similitudes tengan con un auto que se seleccione como referencia. Se deben implementar 3 tipos de busquedas: ingresar la id de un auto para mostrar su información, ingresar la id de un auto para encontrar los 10 mas parecidos en caracteristicas y finalmente ingresar cada una de las caracteristicas del auto para encontrar los 10 autos que más se parezcan en lo ingresado.

# Solución implementada

Para poder lograr lo anterior utilizamos el KD-Tree, el cual es una estructura de datos espacial que permitirá, mediante la busqueda por distancia entre vectores n dimensionales, encontrar los nodos que presenten una distancia euclidiana menor, respecto de un vector predeterminado. Para esta solución además se utilizará una cola con prioridad, la cual permitira ir guardando los 10 nodos que más se parezcan al nodo (o vector) que se este utilizando (o menor distancia euclidiana tengan entre si), que para este caso sera el auto con sus caracteristicas ( vector con números que representan sus caracteristicas, transformados mediante one hot enconding desde el dataset).

# Coevaluación

|Criterio                 | Jose Luis Alonso | Juan Pablo Raab | Diego Acosta |
|-------------------------|------------------|-----------------|----------------|--------------|
|Asistencia y puntualidad |Asiste con puntualidad a todas las reuniones                  |Asiste con puntualidad a todas las reuniones                  |Asiste con puntualidad a todas las reuniones                               |
|Integración              |Se integra bien en el grupo, buena comunicación                  |Se integra bien en el grupo, buena comunicación                  |Se integra bien en el grupo, buena comunicación                 | Se integra bien en el grupo, buena comunicación     | 
|Responsabilidad          | Cumple con todas las tareas que se le asignan                 | Cumple con todas las tareas que se le asignan                  | Cumple con todas las tareas que se le asignan                 |
|Contribución             | Aporta buenas ideas para lograr la solución del problema                 | Aporta buenas ideas para lograr la solución del problema                 |  Aporta buenas ideas para lograr la solución del problema               |
|Resolución de conflictos | Acepta ideas de otros y a la vez aporta las propias. 0 conflictos                 | Acepta ideas de otros y a la vez aporta las propias. 0 conflictos                 | Acepta ideas de otros y a la vez aporta las propias. 0 conflictos                |
|Aspectos postivos        |Demuestra entusiasmo y aporta buenas ideas     | Encuentra errores poco evidentes y aporta soluciones a estos      | Posee un amplio conocimiento de las herramientas utilizadas durante el trabajo, las cuales comparte con el grupo        |
|Aspectos a mejorar        | Avanza demasiado rápido, debe intentar esperar al grupo | Debe familiarizarse con las herramientas de programación, a veces pierde un poco de tiempo en la instalación de estas.  | Debe aportar mas codificando en una próxima entrega, no solo aportar con ideas y solucionar problemas |

- Seleccionar sodoku desde: https://www.sudoku-online.org/
- Link al video: https://drive.google.com/file/d/1ZEuAsBY0VOLxk_di_aFcyyZlnIvOiAgk/view?usp=sharing
