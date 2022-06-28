# Tarea-3
Sistemas Distribuidos







1. Explique la arquitectura que Cassandra maneja. Cuando se crea el clúster ¿Cómo los nodos se conectan? ¿Qué
ocurre cuando un cliente realiza una petición a uno de los nodos? ¿Qué ocurre cuando uno de los nodos se desconecta?
¿La red generada entre los nodos siempre es eficiente? ¿Existe balanceo de carga?

Cassandra maneja la arquitectura peer to peer, el cual permite que al crear el clúster la información se replica a los otros nodos para evitar alguna falla. Los nodos se conectan a través del protocolo Gossip, el cual permite transmitir la información.
Cuando un cliente realiza una petición y esta le llega a un nodo, el cual replicará la información a todos los nodos disponibles, después se derterminará cuantos nodos van a responder la petición para poder visualizar si la petición fue recibida con éxito.
Cuando un nodo se desconecta, se espera que los otros nodos a los que se les envio la copia de petición le responda, ya que al tener más de un nodo con la información, evita que hayan fallas.
Si, la red generada entre los nodos siempre es eficiente, ya que a la hora de que se desconecte un nodo otros nodos tienen copia de la información, los cuales enviarán la información de la petición del cliente.
El balanceo de carga depende de la partición que se escoga, ya que si se escoge la partición aletoria ya que al determinar los pares clave-valor de forma aleatoria genera un buen balanceo de carga, en cambio si se escoge la partición con preservación del orden el cual distribuye de forma natural, no se podrá tener un buen balanceo de carga debido a la distribución irregular de las clave-valor.


2. Cassandra posee principalmente dos estrategias para mantener redundancia en la replicación de datos. ¿Cuáles son
estos? ¿Cuál es la ventaja de uno sobre otro? ¿Cuál utilizaría usted para en el caso actual y por qué? Justifique
apropiadamente su respuesta.

Esta la Estrategia Simple y Estrategia de topología de red, la ventaja es que la estrategia simple al tener un nodo se determinan sus nodos en el sentido de agujas del reloj y en esas se realizará la copia, en cambio la topología de red debe saber primero como se agruparan los datos y después se determinará la estrategia de colocación de copias. Para el caso de la tarea escogería la estrategia simple , ya que se eligirá un nodo y se enviarán las copias correspondientes independiente de la agrupación de datos, debido a que si se modifica la cantidad de pacientes y recetas, no afectará en el calculo de las replicas de información y la elección de los nodos para esto.

3. Teniendo en cuenta el contexto del problema ¿Usted cree que la solución propuesta es la correcta? ¿Qué ocurre
cuando se quiere escalar en la solución? ¿Qué mejoras implementaría? Oriente su respuesta hacia el Sharding (la
replicación/distribución de los datos) y comente una estrategia que podría seguir para ordenar los datos.
Sí, la solución es una propuesta correcta, cuando se quiere escalar la solución primero se implementa cassandra con los datos que se nos dan que son paciente y receta. Para mejorar esto, implementaría la estrategia simple con el fin de que se puedan distribuir los datos y las replicas, para que a la hora de agregar más pacientes y recetas no afecte la distribución de los datos y poder tener un buen balanceo de carga al implementar la solución.
