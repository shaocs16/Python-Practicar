# 100 Ejercicios de Python (Nivel Medio-Difícil)

Este documento contiene 100 ejercicios de Python con variables iniciales y algunas APIs públicas que no requieren autenticación.

---

## Bloque 1: Manipulación de listas y diccionarios (1-20)

```python
usuarios = [
    {"id": 1, "nombre": "Ana", "edad": 28, "ciudad": "Madrid"},
    {"id": 2, "nombre": "Luis", "edad": 35, "ciudad": "Barcelona"},
    {"id": 3, "nombre": "Carlos", "edad": 22, "ciudad": "Valencia"},
    {"id": 4, "nombre": "Elena", "edad": 40, "ciudad": "Sevilla"},
]

productos = [
    {"id": 101, "nombre": "Laptop", "precio": 1200.50, "stock": 5},
    {"id": 102, "nombre": "Monitor", "precio": 320.99, "stock": 12},
    {"id": 103, "nombre": "Teclado", "precio": 45.50, "stock": 30},
    {"id": 104, "nombre": "Mouse", "precio": 25.00, "stock": 25},
]
```

Ejercicios:

1. Listar nombres de usuarios mayores de 30 años.
2. Sumar todas las edades de los usuarios.
3. Filtrar productos con precio mayor a 100.
4. Calcular el stock total de todos los productos.
5. Ordenar usuarios por edad descendente.
6. Crear un diccionario `{nombre: edad}` para todos los usuarios.
7. Buscar un producto por su nombre "Monitor".
8. Aumentar en un 10% el precio de todos los productos.
9. Eliminar usuarios menores de 25 años.
10. Contar cuántos productos tienen stock menor a 10.
11. Crear una lista con el nombre de los productos y su precio formateado `$precio`.
12. Encontrar el usuario con la edad más alta.
13. Comprobar si algún usuario vive en "Sevilla".
14. Crear una lista con los nombres de los usuarios que tengan la letra “a” en su nombre.
15. Cambiar la ciudad de "Carlos" a "Bilbao".
16. Crear un diccionario donde la clave sea la ciudad y el valor la lista de usuarios en esa ciudad.
17. Calcular el precio medio de los productos.
18. Duplicar el stock de todos los productos.
19. Crear una función que reciba un id de producto y devuelva su precio.
20. Generar una lista de nombres de usuarios en mayúsculas.

---

## Bloque 2: Strings y manipulación de texto (21-40)

```python
frases = [
    "Python es un lenguaje de programación muy potente",
    "Aprender a programar requiere práctica y paciencia",
    "Data Science y Machine Learning son campos en auge",
    "El manejo de strings en Python es muy flexible"
]
```

Ejercicios:
21. Contar cuántas veces aparece la letra "a" en todas las frases.
22. Reemplazar "Python" por "PYTHON" en todas las frases.
23. Contar cuántas palabras tiene cada frase.
24. Encontrar la frase más larga en número de caracteres.
25. Crear una lista de todas las palabras que aparecen en las frases.
26. Contar cuántas veces aparece la palabra "programar".
27. Extraer la primera palabra de cada frase.
28. Convertir todas las frases a minúsculas.
29. Eliminar todas las vocales de las frases.
30. Crear un diccionario `{frase: número_de_palabras}`.
31. Ordenar las frases por longitud.
32. Comprobar si alguna frase contiene "Machine Learning".
33. Unir todas las frases en un solo string separado por punto y espacio.
34. Contar cuántas palabras únicas hay en todas las frases.
35. Crear una función que reciba una frase y devuelva las palabras invertidas.
36. Contar cuántos caracteres totales tienen todas las frases juntas.
37. Crear un resumen con las primeras 10 letras de cada frase.
38. Revertir cada frase letra por letra.
39. Comprobar si alguna frase empieza con "Data".
40. Convertir todas las frases en listas de palabras.

---

## Bloque 3: Funciones, ciclos y lógica (41-60)

```python
numeros = [12, 7, 25, 3, 19, 8, 10, 15]
```

Ejercicios:
41. Calcular la suma de todos los números.
42. Encontrar el número mayor y menor.
43. Crear una función que devuelva True si un número es primo.
44. Filtrar los números pares de la lista.
45. Calcular el promedio de los números.
46. Crear una lista con el cuadrado de cada número.
47. Crear un diccionario `{numero: numero*2}`.
48. Ordenar los números de mayor a menor.
49. Crear una función que reciba una lista y devuelva la mediana.
50. Contar cuántos números son mayores que 10.
51. Generar una lista con los números multiplicados por su índice.
52. Crear un ciclo que imprima todos los números hasta 20 usando `while`.
53. Sumar solo los números impares.
54. Crear una función que devuelva el factorial de un número.
55. Verificar si la lista está ordenada de menor a mayor.
56. Reemplazar todos los números mayores a 15 por 15.
57. Crear una lista con números al cubo.
58. Contar cuántos números son múltiplos de 5.
59. Crear una función que devuelva la lista invertida sin usar `.reverse()`.
60. Crear un diccionario que cuente cuántos números pares e impares hay.

---

## Bloque 4: APIs públicas sin token (61-80)

APIs públicas:

* Pokémon: `https://pokeapi.co/api/v2/pokemon/{nombre}`
* Dog API: `https://dog.ceo/api/breeds/image/random`
* Numbers API: `http://numbersapi.com/{numero}/math`

Ejercicios:
61. Llamar a la API Pokémon para "pikachu" y mostrar sus tipos.
62. Obtener una imagen aleatoria de un perro y guardarla localmente.
63. Llamar a la Numbers API para el número 42 y mostrar el texto.
64. Crear una función que reciba un nombre de Pokémon y devuelva su peso.
65. Obtener los 3 primeros movimientos de "charmander".
66. Obtener la raza de un perro a partir de la URL de la imagen.
67. Crear un diccionario con 5 números y sus datos de la Numbers API.
68. Contar cuántas letras tiene la especie de un Pokémon.
69. Mostrar el nombre de todos los tipos de un Pokémon.
70. Llamar a la Numbers API para 5 números aleatorios.
71. Guardar 3 URLs de imágenes de perros en una lista.
72. Crear una función que devuelva `True` si un Pokémon es de tipo "fire".
73. Mostrar la URL de la imagen oficial de "bulbasaur".
74. Hacer una lista de nombres de 5 Pokémon y sus pesos.
75. Comprobar si algún Pokémon de la lista es legendario.
76. Contar cuántos movimientos tiene un Pokémon.
77. Crear un mini-juego que pregunte el tipo de un Pokémon y diga si es correcto.
78. Crear un loop que llame a 3 Pokémon y devuelva sus habilidades.
79. Obtener una frase divertida de la Numbers API para tu edad.
80. Guardar en un archivo `pokemons.txt` los nombres de 10 Pokémon.

---

## Bloque 5: Clases y objetos (81-100)

```python
class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

personas = [
    Persona("Ana", 28, "Madrid"),
    Persona("Luis", 35, "Barcelona"),
    Persona("Carlos", 22, "Valencia"),
    Persona("Elena", 40, "Sevilla"),
]
```

Ejercicios:
81. Crear un método que imprima "Hola, mi nombre es X".
82. Crear un método que aumente la edad en 1.
83. Crear una lista con los nombres de todas las personas.
84. Ordenar las personas por edad usando un método.
85. Crear una clase Producto con nombre, precio y stock.
86. Crear un método que disminuya el stock en 1.
87. Crear un método que aumente el precio en un porcentaje dado.
88. Crear una función que reciba una lista de Personas y devuelva la más joven.
89. Crear una función que filtre personas por ciudad.
90. Crear una función que genere un diccionario `{nombre: ciudad}` de las personas.
91. Añadir un atributo "email" a cada Persona.
92. Crear un método que devuelva True si la persona es mayor de edad.
93. Crear una clase Coche con marca, modelo y km.
94. Crear un método que recorra cierta distancia y aumente km.
95. Crear un método que imprima la info del coche.
96. Crear una clase Estudiante que herede de Persona e incluya notas.
97. Crear un método para calcular la media de las notas.
98. Crear un método que diga si el estudiante aprueba (>5).
99. Crear una lista de 5 estudiantes con notas y calcular la media general.
100. Crear un método `__str__` para imprimir la información de cualquier objeto de manera bonita.
