# Crear un Diccionario
informacion_personal = {
    "nombre": "Stalin Guachizaca",
    "edad": 40,
    "ciudad": "Guayaquil",
    "profesion": "Ingeniero de Software"
}

# Acceder y Modificar Valores
# Acceder al valor asociado con la clave "ciudad"
ciudad_actual = informacion_personal["ciudad"]
print(f"Ciudad actual: {ciudad_actual}")

# Modificar la ciudad
informacion_personal["ciudad"] = "Quito"
print(f"Nueva ciudad: {informacion_personal['ciudad']}")

# Agregar una nueva clave-valor para la profesión
informacion_personal["profesion"] = "Desarrollador Web"

# Verificar Existencia de Claves
if "telefono" not in informacion_personal:
    # Si no existe, agregar un número de teléfono ficticio
    informacion_personal["telefono"] = "0991234567"

# Eliminar una Clave
# Eliminar la clave "edad"
del informacion_personal["edad"]

# Imprimir el Diccionario Final
print("Diccionario final:")
print(informacion_personal)
