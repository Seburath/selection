
# Que hice?

1 - Al abrir el script y verlo superficialmente me pude fijar que si hay algo con lo que no estabamos cumpliendo era con DRY, don't repeat yourself, algo que podriamos lograr facilmente ya que todas las paginas de los exchanges seguian un mismo patron.

2 - Removi la numeracion de paginas que estaba hardcoded, esto permitio simplificar el codigo y hacerlo extensible a otros exchanges, ya podremos salirnos de los principales de Estados Unidos y meternos con otros mercados facilmente, como el LSE en Reino Unido o el TSE en Canada solo con añadir el code de dichos exchanges.

3 - Añadi la insercion a la DB con ayuda del ORM Peewee, que da una interfaz bastante simple para manejar bases de datos desde Python.


# Lo que no entendí

1 - En esta linea `range(ran_ini,ran_end)[0::4]` no pude entender la necesidad de hacer incrementos de 4 en 4.


# Lo que asumí
1 - En la tabla cree una columna llamada routing, ya que en el codigo previo vi que estaba predefinido el termino SMART, que asumí que hacia referencia al order routing al comprar algo en el stock market, sobre como se ejecuta esa orden. Puede que este resumiendo mucho el termino pero [acá explica mejor a que me refiero.](https://en.wikipedia.org/wiki/Smart_order_routing)

* Cuando imprime STK junto con los valores del simbolo no tengo idea a que se refiere, asumí que era algún acronimo para STK, sin embargo lo dejé como unknown_field en la DB.

# Que mejoraria si tuviese mas tiempo? 
* Aunque mi refactoring mejoro la implementacion en muchos aspectos tal vez podriamos mejorar los tiempos de ejecucion y pensar en un manejo de errores, aunque dependiendo del caso de uso que se tenga en mente esta lista podria crecer aún más.