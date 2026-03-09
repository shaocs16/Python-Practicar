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


## Ejercicio 1
## Mostrar nombres de usuarios mayores de 30 años
list_user_mayor_30 = list()

for user in usuarios:
    if user["edad"] > 30:
        list_user_mayor_30.append(user["nombre"])

print("###############")
print("Ejercicio 1")
print("###############")
print(f"Los nombres son {','.join(list_user_mayor_30)}")

## Ejercico 2
## Sumar todas las edades de los usuarios.
suma = 0

for edad in usuarios:
    suma += edad["edad"]

print("###############")
print("Ejercicio 2")
print("###############")
print(f"La edad todad sumada es {suma}")

