import numpy as np
import pandas as pd
from inline_sql import sql, sql_val
import matplotlib.pyplot as plt


equipos = pd.read_csv('enunciado_equipos.csv')
jugadores = pd.read_csv('enunciado_jugadores.csv')
atributos = pd.read_csv('enunciado_jugadores_atributos.csv')
liga = pd.read_csv('enunciado_liga.csv')
paises = pd.read_csv('enunciado_paises.csv')
partidos = pd.read_csv('enunciado_partidos.csv')


consulta2012 = """
            SELECT DISTINCT country_id,date,season,home_team_api_id, away_team_api_id, home_team_goal, away_team_goal
            FROM 'enunciado_partidos.csv'
            WHERE (country_id = 13274) and (season = '2012/2013')
            ORDER BY date ASC

"""
data2012 = sql^ consulta2012

consulta2013 = """
            SELECT DISTINCT country_id,date,season,home_team_api_id, away_team_api_id, home_team_goal, away_team_goal
            FROM 'enunciado_partidos.csv'
            WHERE (country_id = 13274) and (season = '2013/2014')
            ORDER BY date ASC

"""
data2013 = sql^ consulta2013

consulta2014 = """
            SELECT DISTINCT country_id,date,season,home_team_api_id, away_team_api_id, home_team_goal, away_team_goal
            FROM 'enunciado_partidos.csv'
            WHERE (country_id = 13274) and (season = '2014/2015')
            ORDER BY date ASC

"""
data2014 = sql^ consulta2014
consulta2015 = """
            SELECT DISTINCT country_id,date,season,home_team_api_id, away_team_api_id, home_team_goal, away_team_goal
            FROM 'enunciado_partidos.csv'
            WHERE (country_id = 13274) and (season = '2015/2016')
            ORDER BY date ASC

"""
data2015 = sql^ consulta2015

consulta = """
            SELECT DISTINCT home_team_api_id,season, SUM(home_team_goal), SUM(away_team_goal)
            FROM 'enunciado_partidos.csv'
            WHERE (country_id = 13274)
            GROUP BY home_team_api_id,season

"""
data_equipos = sql^ consulta

consulta2 = """
            SELECT DISTINCT away_team_api_id,season, SUM(home_team_goal), SUM(away_team_goal)
            FROM 'enunciado_partidos.csv'
            WHERE (country_id = 13274)
            GROUP BY away_team_api_id,season

"""
data_equipos_visitantes = sql^ consulta2

data_equipos.rename({'home_team_api_id':'team_api_id','sum(home_team_goal)': 'Favor','sum(away_team_goal)':'Contra'}, axis = 'columns', inplace=True)
data_equipos = data_equipos.set_index(['team_api_id','season'])
data_equipos_visitantes.rename({'away_team_api_id':'team_api_id','sum(away_team_goal)': 'Favor','sum(home_team_goal)':'Contra'}, axis = 'columns', inplace=True)
data_equipos_visitantes = data_equipos_visitantes.set_index(['team_api_id','season'])

df1 = data_equipos + data_equipos_visitantes

plt.figure(figsize=(20,5))

plt.bar(range(len(df1['team_api_id'])),df1, 
color=np.where(df1 < 0, 'crimson', 'steelblue') #Color dependiendo de si es positivo o negativo
)

plt.xticks(range(len(df1['team_api_id'])),df1['team_api_id'],rotation=45)

plt.title('Variación de producción', fontsize=20, fontweight='bold')

# Agrego los valores encima de cada barra
for idx, value in enumerate(df1):
    plt.text(idx, value + (0.01 if value >= 0 else -0.05), 
             f'{value:.2f}', ha='center', va='bottom' if value >= 0 else 'top', fontsize=9)

# Mejoro el estilo de los ejes
plt.xlabel('Sectores', fontsize=15)
plt.ylabel('Variación', fontsize=15)

plt.show()