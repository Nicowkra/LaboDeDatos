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




#-----------------------------#


consulta = """
            SELECT DISTINCT home_team_api_id, team_long_name,SUM(home_team_goal), SUM(away_team_goal)
            FROM 'enunciado_partidos.csv' AS partidos
            INNER JOIN 'enunciado_equipos.csv' AS equipos ON partidos.home_team_api_id = equipos.team_api_id
            WHERE (country_id = 13274) and (season = '2012/2013')
            GROUP BY home_team_api_id,season,team_long_name

"""
data_local_2012 = sql^ consulta

consulta = """
            SELECT DISTINCT away_team_api_id, team_long_name,SUM(home_team_goal), SUM(away_team_goal)
            FROM 'enunciado_partidos.csv' AS partidos
            INNER JOIN 'enunciado_equipos.csv' AS equipos ON partidos.away_team_api_id = equipos.team_api_id
            WHERE (country_id = 13274) and (season = '2012/2013')
            GROUP BY away_team_api_id,season,team_long_name


"""
data_visitantes_2012 = sql^ consulta

consulta = """
            SELECT DISTINCT home_team_api_id, team_long_name,SUM(home_team_goal), SUM(away_team_goal)
            FROM 'enunciado_partidos.csv' AS partidos
            INNER JOIN 'enunciado_equipos.csv' AS equipos ON partidos.home_team_api_id = equipos.team_api_id
            WHERE (country_id = 13274) and (season = '2013/2014')
            GROUP BY home_team_api_id,season,team_long_name


"""
data_local_2013 = sql^ consulta

consulta = """
            SELECT DISTINCT away_team_api_id, team_long_name,SUM(home_team_goal), SUM(away_team_goal)
            FROM 'enunciado_partidos.csv' AS partidos
            INNER JOIN 'enunciado_equipos.csv' AS equipos ON partidos.away_team_api_id = equipos.team_api_id
            WHERE (country_id = 13274) and (season = '2013/2014')
            GROUP BY away_team_api_id,season,team_long_name


"""
data_visitantes_2013 = sql^ consulta

consulta = """
            SELECT DISTINCT home_team_api_id, team_long_name,SUM(home_team_goal), SUM(away_team_goal)
            FROM 'enunciado_partidos.csv' AS partidos
            INNER JOIN 'enunciado_equipos.csv' AS equipos ON partidos.home_team_api_id = equipos.team_api_id
            WHERE (country_id = 13274) and (season = '2014/2015')
            GROUP BY home_team_api_id,season,team_long_name


"""
data_local_2014 = sql^ consulta

consulta = """
            SELECT DISTINCT away_team_api_id, team_long_name,SUM(home_team_goal), SUM(away_team_goal)
            FROM 'enunciado_partidos.csv' AS partidos
            INNER JOIN 'enunciado_equipos.csv' AS equipos ON partidos.away_team_api_id = equipos.team_api_id
            WHERE (country_id = 13274) and (season = '2014/2015')
            GROUP BY away_team_api_id,season,team_long_name


"""
data_visitantes_2014 = sql^ consulta

consulta = """
            SELECT DISTINCT home_team_api_id, team_long_name,SUM(home_team_goal), SUM(away_team_goal)
            FROM 'enunciado_partidos.csv' AS partidos
            INNER JOIN 'enunciado_equipos.csv' AS equipos ON partidos.home_team_api_id = equipos.team_api_id
            WHERE (country_id = 13274) and (season = '2015/2016')
            GROUP BY home_team_api_id,season,team_long_name


"""
data_local_2015 = sql^ consulta

consulta = """
            SELECT DISTINCT away_team_api_id, team_long_name,SUM(home_team_goal), SUM(away_team_goal)
            FROM 'enunciado_partidos.csv' AS partidos
            INNER JOIN 'enunciado_equipos.csv' AS equipos ON partidos.away_team_api_id = equipos.team_api_id
            WHERE (country_id = 13274) and (season = '2015/2016')
            GROUP BY away_team_api_id,season,team_long_name


"""
data_visitantes_2015 = sql^ consulta

#------------------------------

data_local_2012.rename({'home_team_api_id':'team_api_id','team_long_name':'Equipo','sum(home_team_goal)': 'Favor_2012','sum(away_team_goal)':'Contra_2012'}, axis = 'columns', inplace=True)
data_local_2012 = data_local_2012.set_index(['team_api_id','Equipo'])
data_visitantes_2012.rename({'away_team_api_id':'team_api_id','team_long_name':'Equipo','sum(away_team_goal)': 'Favor_2012','sum(home_team_goal)':'Contra_2012'}, axis = 'columns', inplace=True)
data_visitantes_2012 = data_visitantes_2012.set_index(['team_api_id','Equipo'])

data_local_2013.rename({'home_team_api_id':'team_api_id','team_long_name':'Equipo','sum(home_team_goal)': 'Favor_2013','sum(away_team_goal)':'Contra_2013'}, axis = 'columns', inplace=True)
data_local_2013 = data_local_2013.set_index(['team_api_id','Equipo'])
data_visitantes_2013.rename({'away_team_api_id':'team_api_id','team_long_name':'Equipo','sum(away_team_goal)': 'Favor_2013','sum(home_team_goal)':'Contra_2013'}, axis = 'columns', inplace=True)
data_visitantes_2013 = data_visitantes_2013.set_index(['team_api_id','Equipo'])

data_local_2014.rename({'home_team_api_id':'team_api_id','team_long_name':'Equipo','sum(home_team_goal)': 'Favor_2014','sum(away_team_goal)':'Contra_2014'}, axis = 'columns', inplace=True)
data_local_2014 = data_local_2014.set_index(['team_api_id','Equipo'])
data_visitantes_2014.rename({'away_team_api_id':'team_api_id','team_long_name':'Equipo','sum(away_team_goal)': 'Favor_2014','sum(home_team_goal)':'Contra_2014'}, axis = 'columns', inplace=True)
data_visitantes_2014 = data_visitantes_2014.set_index(['team_api_id','Equipo'])

data_local_2015.rename({'home_team_api_id':'team_api_id','team_long_name':'Equipo','sum(home_team_goal)': 'Favor_2015','sum(away_team_goal)':'Contra_2015'}, axis = 'columns', inplace=True)
data_local_2015 = data_local_2015.set_index(['team_api_id','Equipo'])
data_visitantes_2015.rename({'away_team_api_id':'team_api_id','team_long_name':'Equipo','sum(away_team_goal)': 'Favor_2015','sum(home_team_goal)':'Contra_2015'}, axis = 'columns', inplace=True)
data_visitantes_2015 = data_visitantes_2015.set_index(['team_api_id','Equipo'])

df2012 = data_local_2012 + data_visitantes_2012
df2013 = data_local_2013 +data_visitantes_2013
df2014 = data_local_2014 + data_visitantes_2014
df2015 = data_local_2015 + data_visitantes_2015

plt.rcParams["figure.figsize"] = (20,7)
df = pd.merge(df2012,df2013,on ='team_api_id',how = 'outer')
df1 = pd.merge(df2014,df2015,on ='team_api_id',how = 'outer')
df2 = pd.merge(df,df1,on = 'team_api_id',how = 'outer')
df2 = df2[['Favor_2012','Favor_2013','Favor_2014','Favor_2015','Contra_2012','Contra_2013','Contra_2014','Contra_2015']]
df2.sort_index()

df2_favor = df2.drop(['Contra_2012','Contra_2013','Contra_2014','Contra_2015'],axis = 1)
df2_contra = df2.drop(['Favor_2012','Favor_2013','Favor_2014','Favor_2015'],axis = 1)

fig, axes = plt.subplots(1, 2)

ax1 = df2_favor.plot(kind= 'bar',x = 'Equipos',use_index=True,width = 0.7 ,color = ['deeppink','orchid','blueviolet','royalblue'],ax=axes[0],xlabel='Goles a favor')
ax2 = df2_contra.plot(kind= 'bar',use_index=True,width = 0.7 ,color = ['yellow','goldenrod','orangered','maroon'],ax=axes[1],xlabel ='Goles en contra')


plt.show()


#---------------------------------
cols_to_sum_favor = df2_favor.columns[ : df2_favor.shape[1]]
cols_to_sum_contra = df2_contra.columns[ : df2_contra.shape[1]]
df2_favor['Favor_Promedio'] = df2_favor[cols_to_sum_favor].sum(axis = 1) / df2_favor.count(axis = 1)
df2_contra['Contra_Promedio']= df2_contra[cols_to_sum_contra].sum(axis = 1)/df2_contra.count(axis = 1)

df_promedio = pd.merge(df2_favor,df2_contra,on ='team_api_id',how = 'outer')
df_promedio = df_promedio.drop(['Favor_2012','Favor_2013','Favor_2014','Favor_2015','Contra_2012','Contra_2013','Contra_2014','Contra_2015'],axis = 1)

df_promedio.plot(kind='bar',use_index = True,width = 0.7 ,color = ['orchid','blueviolet','royalblue'] )
