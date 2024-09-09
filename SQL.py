# Importamos bibliotecas
import pandas as pd
from inline_sql import sql, sql_val


#%%===========================================================================
# Importamos los datasets que vamos a utilizar en este programa
#=============================================================================

carpeta = "~/Descargas/SQL_/"

# Ejercicios AR-PROJECT, SELECT, RENAME
empleado       = pd.read_csv(carpeta+"empleado.csv")
# Ejercicios AR-UNION, INTERSECTION, MINUS
alumnosBD      = pd.read_csv(carpeta+"alumnosBD.csv")
alumnosTLeng   = pd.read_csv(carpeta+"alumnosTLeng.csv")
# Ejercicios AR-CROSSJOIN
persona        = pd.read_csv(carpeta+"persona.csv")
nacionalidades = pd.read_csv(carpeta+"nacionalidades.csv")
# Ejercicios ¿Mismos Nombres?
se_inscribe_en=pd.read_csv(carpeta+"se_inscribe_en.csv")
materia       =pd.read_csv(carpeta+"materia.csv")
# Ejercicio JOIN múltiples tablas
vuelo      = pd.read_csv(carpeta+"vuelo.csv")    
aeropuerto = pd.read_csv(carpeta+"aeropuerto.csv")    
pasajero   = pd.read_csv(carpeta+"pasajero.csv")    
reserva    = pd.read_csv(carpeta+"reserva.csv")    
# Ejercicio JOIN tuplas espúreas
empleadoRol= pd.read_csv(carpeta+"empleadoRol.csv")    
rolProyecto= pd.read_csv(carpeta+"rolProyecto.csv")    
# Ejercicios funciones de agregación, LIKE, Elección, Subqueries 
# y variables de Python
examen     = pd.read_csv(carpeta+"examen.csv")
# Ejercicios de manejo de valores NULL
examen03 = pd.read_csv(carpeta+"examen03.csv")
#1
consultaSQL = """
SELECT Nombre, Codigo
FROM aeropuerto
WHERE Ciudad = 'Londres'
              """

dataframeResultado = sql^ consultaSQL
print(dataframeResultado)
print("------------------")

#2
#Paris

#3
consultaSQL = """
SELECT Numero
FROM vuelo
WHERE Origen = 'CDG' and Destino= 'LHR'
              """

dataframeResultado = sql^ consultaSQL
print(dataframeResultado)
print("------------------")

#4
consultaSQL = """
SELECT Numero
FROM vuelo
WHERE (Origen = 'CDG' and Destino= 'LHR') or (Origen = 'LHR' and Destino= 'CDG')
              """

dataframeResultado = sql^ consultaSQL
print(dataframeResultado)
print("------------------")

#5
consultaSQL = """
SELECT Fecha
FROM reserva
WHERE Precio >200
              """

dataframeResultado = sql^ consultaSQL
print(dataframeResultado)
print("------------------")


#2.1
consultaSQL = """
Select Numero
FROM vuelo
INTERSECT
Select NroVuelo
FROM reserva
"""

dataframeResultado = sql^ consultaSQL
print(dataframeResultado)
print("------------------")

#2.2
consultaSQL = """
Select Numero
FROM vuelo
EXCEPT
Select NroVuelo
FROM reserva
"""

dataframeResultado = sql^ consultaSQL
print(dataframeResultado)
print("------------------")

#2.3
consultaSQL = """

Select Origen  AS ngkdalngklda
FROM vuelo
UNION 
Select Destino
FROM vuelo
INTERSECT
Select Codigo
FROM aeropuerto
"""

dataframeResultado = sql^ consultaSQL
print(dataframeResultado)
print("------------------")

#3.1
consultaSQL = """

Select a.Nombre
FROM aeropuerto as a
INNER JOIN vuelo as v
ON v.Origen = a.Codigo
WHERE v.Numero = 165
"""

dataframeResultado = sql^ consultaSQL
print(dataframeResultado)
print("------------------")

#3.2
consultaSQL = """
SELECT DISTINCT p.Nombre
FROM pasajero as p
INNER JOIN reserva as r
ON p.DNI = r.DNI
WHERE r.Precio < 200
"""

dataframeResultado = sql^ consultaSQL
print(dataframeResultado)
print("------------------")

#3.3
consultaSQL = """

SELECT  p.Nombre,r.Fecha,v.Destino
FROM pasajero as p
INNER JOIN reserva as r
ON p.DNI = r.DNI
INNER JOIN vuelo as v
ON v.Numero = r.NroVuelo
WHERE Origen = 'MAD'
"""

dataframeResultado = sql^ consultaSQL
print(dataframeResultado)
print("------------------")

#4
consultaSQL = """

SELECT DISTINCT p.Nombre,r.Fecha,v.Destino
FROM pasajero as p
INNER JOIN reserva as r
ON p.DNI = r.DNI
INNER JOIN vuelo as v
ON v.Numero = r.NroVuelo
WHERE Origen = 'MAD'
"""

dataframeResultado = sql^ consultaSQL
print(dataframeResultado)
print("------------------")