Problema 1 (7pts):
Realiza un algoritmo recursivo que dada la siguiente cadena elimine los números y caracteres especiales e imprima la oración oculta.
cadena= '''
312313L....:;;;A;;;;;1231231231231313131 RE13123123
1313??????**\*\***C12312312312313
U;;;;R???S23123
12312312I.....V44515
454%###I####DAD)))))))))))))
((((((((((((((((((())))))
))))))))))))) ES{}}}}}}} ,,,<<>>>>>>>G@@@@@E
{{{{{{{{{{{{{{{NI}}}}}}}}}}}}}}}!!!!!!!$$$$$A......
........................L!!!!

'''

Problema 2 (13pts):
Una floristería te ha contratado para digitalizar su negocio, por lo que debes desarrollar un software que cumpla con los siguientes requerimientos:
Módulo administrativo:
Agregar productos: tendrás una estructura de datos con la información del inventario actual de la floristería; esta información debe modelarse como objetos y guardarse en una nueva estructura de datos, que será sobre la que trabajarás el resto del programa. Esta acción debe ocurrir automáticamente apenas se inicia el programa, y debe poder repetirse a partir del menú principal. Hay dos tipos de productos: flores y semillas.
Ver productos: mostrando por pantalla de forma ordenada cada uno de los productos del local con su detalle.
Módulo de distribución de inventario:
La floristería tiene dos vendedores, y cada uno tiene una lista de ventas registradas. La primera lista está ordenada de forma ascendente y la segunda de forma descendente (según la cantidad de items comprados). Genera una nueva lista ordenada en forma ascendente que guarde todos los elementos de ambas listas anteriores y actualiza el stock de productos a partir de las ventas registradas. (No se puede utilizar el método .sort() de arrays, ni la built-in function sorted(), ni algoritmos de ordenamiento).
Debes trabajar con funciones y con programación orientada a objetos, recordando que cada clase debe definirse en un archivo diferente.

products = [
{ “id”: 1, “name”: “Rose”, type: “flower”, “stock”: 160, “colors”: [“red”, “white”, “pink”] },
{ “id”: 2, “name”: “Tulip”, type: “flower”, “stock”: 34, “colors”: [“white”, “yellow”] },
{ “id”: 3, “name”: “Sunflower seeds”, type: “seeds”, “stock”: 50 },
{ “id”: 4, “name”: “Sunflower”, type: “flower”, “stock”: 77, “colors”: [“yellow”] },
{ “id”: 5, “name”: “Lavender seeds”, type: “seeds”, “stock”: 100, “colors”: [“purple”] },
{ “id”: 6, “name”: “Carnation”, type: “flower”, “stock”: 89, “colors”: [“yellow”, “burgundy”, “purple”, “pink”, “red”, “white”] },
]

vendor_1 = [
{ “product_id”: 5, “customer_id”: 333, “amnt”: 1 },
{ “product_id”: 5, “customer_id”: 1010, “amnt”: 2 },
{ “product_id”: 3, “customer_id”: 1111, “amnt”: 3 },
{ “product_id”: 2, “customer_id”: 222, “amnt”: 6 },
{ “product_id”: 6, “customer_id”: 444, “amnt”: 7 },
{ “product_id”: 1, “customer_id”: 1111, “amnt”: 20 },
]

vendor_2 = [
{ “product_id”: 6, “customer_id”: 888, “amnt”: 10 },
{ “product_id”: 1, “customer_id”: 123, “amnt”: 5 },
{ “product_id”: 2, “customer_id”: 321, “amnt”: 4 },
{ “product_id”: 4, “customer_id”: 555, “amnt”: 2 },
{ “product_id”: 1, “customer_id”: 777, “amnt”: 1 },
]
