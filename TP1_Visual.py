import pandas as pd
import numpy as np
from inline_sql import sql, sql_val

carpeta = '/home/Estudiante/Descargas/Tablas/'
equipos = pd.read_csv(carpeta+'enunciado_equipos.csv')
jugadores = pd.read_csv(carpeta+'enunciado_jugadores.csv')
atributos = pd.read_csv(carpeta+'enunciado_jugadores_atributos.csv')
liga = pd.read_csv(carpeta+'enunciado_liga.csv')
paises = pd.read_csv(carpeta+'enunciado_paises.csv')
partidos = pd.read_csv(carpeta+'enunciado_partidos.csv')


consulta2012 = """
            SELECT DISTINCT country_id,date,season,home_team_api_id, away_team_api_id, home_team_goal, away_team_goal
            FROM partidos
            WHERE (country_id = 13274) and (season = '2012/2013' OR season = '2013/2014' OR season = '2014/2015' OR season = '2015/2016')
            ORDER BY date ASC

"""
data = sql^ consulta2012
consulta2013 = """
            SELECT DISTINCT country_id,date,season,home_team_api_id, away_team_api_id, home_team_goal, away_team_goal
            FROM partidos
            WHERE (country_id = 13274) and (season = '2012/2013' OR season = '2013/2014' OR season = '2014/2015' OR season = '2015/2016')
            ORDER BY date ASC

"""
data = sql^ consulta2013
consulta2014 = """
            SELECT DISTINCT country_id,date,season,home_team_api_id, away_team_api_id, home_team_goal, away_team_goal
            FROM partidos
            WHERE (country_id = 13274) and (season = '2012/2013' OR season = '2013/2014' OR season = '2014/2015' OR season = '2015/2016')
            ORDER BY date ASC

"""
data = sql^ consulta2014
consulta2015 = """
            SELECT DISTINCT country_id,date,season,home_team_api_id, away_team_api_id, home_team_goal, away_team_goal
            FROM partidos
            WHERE (country_id = 13274) and (season = '2012/2013' OR season = '2013/2014' OR season = '2014/2015' OR season = '2015/2016')
            ORDER BY date ASC

"""
data = sql^ consulta2015
consulta2 = """
            SELECT DISTINCT home_team_api_id
            from data

"""
data_equipos = sql^ consulta2
dic = {}
equipos_NL = data_equipos['home_team_api_id'].values
def calc_goles(data)
    for i in equipos_NL:
        print(i)
        for j in data.loc[data['home_team_api_id']==i,'home_team_goal'].values:
            if i in dic:
                dic[i] = dic[i]+j
            else:
                dic[i] = j
    return dic
print(dic)
