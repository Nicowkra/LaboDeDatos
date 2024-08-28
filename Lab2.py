nombre_archivo = "Arboles.csv"

def leer_parque(file,parque):
    f = open(nombre_archivo)
    filas = csv.reader(f)
    encabezado = next(filas) # un paso del iterador
    print(encabezado)
    for fila in filas: # ahora el iterador sigue desde la segunda fila
        pass
    f.close()

leer_parque(nombre_archivo,"GENERAL PAZ")