# Escritura de archivo de texto

# Abrimos (o creamos) el archivo my_notes.txt en modo de escritura ('w').
# El modo 'w' sobreescribirá el archivo si ya existe, si no, lo creará.
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales en el archivo.
    file.write("Primera nota: Recuerda estudiar programación todos los días.\n")
    file.write("Segunda nota: Practicar Python mejora las habilidades lógicas.\n")
    file.write("Tercera nota: No olvides revisar las tareas pendientes.\n")

# Una vez terminada la escritura, el archivo se cierra automáticamente por el bloque 'with'.

# Lectura de archivo de texto

# Abrimos el archivo my_notes.txt en modo de lectura ('r').
with open('my_notes.txt', 'r') as file:
    # Leemos y mostramos el contenido línea por línea usando readline().
    # La función readline() lee una línea a la vez.
    print("Contenido del archivo my_notes.txt:")
    line = file.readline()  # Lee la primera línea
    while line:  # Sigue leyendo hasta llegar al final del archivo
        print(line.strip())  # .strip() quita los saltos de línea adicionales al imprimir
        line = file.readline()  # Lee la siguiente línea

# El archivo se cierra automáticamente al salir del bloque 'with'.

# Fin del programa.
