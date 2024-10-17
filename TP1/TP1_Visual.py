import numpy as np
import pandas as pd
from inline_sql import sql, sql_val
import matplotlib.pyplot as plt
import seaborn as sns


equipos = pd.read_csv('enunciado_equipos.csv')
jugadores = pd.read_csv('enunciado_jugadores.csv')
atributos = pd.read_csv('enunciado_jugadores_atributos.csv')
liga = pd.read_csv('enunciado_liga.csv')
paises = pd.read_csv('enunciado_paises.csv')
partidos = pd.read_csv('enunciado_partidos.csv')
pertenece_a = pd.read_csv('pertenece_a.csv')




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

#--------------------------Limpiado de Dataframes--------------------------------------

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


df1 = pd.merge(df2012,df2013,on =['team_api_id','Equipo'],how = 'outer')
df2 = pd.merge(df2014,df2015,on =['team_api_id','Equipo'],how = 'outer')
df = pd.merge(df1,df2,on = ['team_api_id','Equipo'],how = 'outer')
df = df[['Favor_2012','Favor_2013','Favor_2014','Favor_2015','Contra_2012','Contra_2013','Contra_2014','Contra_2015']]
df.sort_index()

df_favor = df.drop(['Contra_2012','Contra_2013','Contra_2014','Contra_2015'],axis = 1)
df_contra = df.drop(['Favor_2012','Favor_2013','Favor_2014','Favor_2015'],axis = 1)

df_favor = df_favor.droplevel('team_api_id')
df_contra = df_contra.droplevel('team_api_id')
                               
#--------------------------Grafico 1--------------------------------------

plt.rcParams["figure.figsize"] = (20,7)
fig, axes = plt.subplots(1, 2)
fig.suptitle('Comparación de goles a lo largo de 4 temporadas', fontsize=16)

ax1 = df_favor.plot(kind= 'bar',use_index=True,width = 0.85 ,color = ['deeppink','orchid','blueviolet','royalblue'],ax=axes[0],xlabel='Goles a favor',fontsize = 10)
ax2 = df_contra.plot(kind= 'bar',use_index=True,width = 0.85 ,color = ['#003f5c','#7a5195','#ef5675','#ffa600'],ax=axes[1],xlabel ='Goles en contra')


plt.show()


#--------------------------Grafico 2--------------------------------------

cols_to_sum_favor = df_favor.columns[ : df_favor.shape[1]]
cols_to_sum_contra = df_contra.columns[ : df_contra.shape[1]]
df_favor['Favor_Promedio'] = df_favor[cols_to_sum_favor].sum(axis = 1) / df_favor.count(axis = 1)
df_contra['Contra_Promedio']= df_contra[cols_to_sum_contra].sum(axis = 1)/df_contra.count(axis = 1)

df_promedio = pd.merge(df_favor,df_contra,on ='Equipo',how = 'outer')
df_promedio = df_promedio.drop(['Favor_2012','Favor_2013','Favor_2014','Favor_2015','Contra_2012','Contra_2013','Contra_2014','Contra_2015'],axis = 1)
fig, axes = plt.subplots()
fig.suptitle('Promedio de goles a favor y en contra', fontsize=16)
df_promedio.plot(kind='bar',use_index = True,width = 0.85 ,color = ['steelblue','coral'], ax = axes )

#--------------------------Grafico 3--------------------------------------

df_local1= pd.merge(data_local_2012,data_local_2013,on =['team_api_id','Equipo'],how = 'outer')
df_local2= pd.merge(data_local_2014,data_local_2015,on =['team_api_id','Equipo'],how = 'outer')
df_local= pd.merge(df_local1,df_local2,on =['team_api_id','Equipo'],how = 'outer')

df_visitante1= pd.merge(data_visitantes_2012,data_visitantes_2013,on =['team_api_id','Equipo'],how = 'outer')
df_visitante2= pd.merge(data_visitantes_2014,data_visitantes_2015,on =['team_api_id','Equipo'],how = 'outer')
df_visitante= pd.merge(df_visitante1,df_visitante2,on =['team_api_id','Equipo'],how = 'outer')

df_local = df_local.drop(['Contra_2012','Contra_2013','Contra_2014','Contra_2015'],axis = 1)
df_visitante = df_visitante.drop(['Contra_2012','Contra_2013','Contra_2014','Contra_2015'],axis = 1)
df_local = df_local.droplevel('team_api_id')
df_visitante = df_visitante.droplevel('team_api_id')
df_local.rename({'Favor_2012':'Temporada 2012','Favor_2013':'Temporada 2013','Favor_2014':'Temporada 2014','Favor_2015':'Temporada 2015',}, axis = 'columns', inplace=True)
df_visitante.rename({'Favor_2012':'Temporada 2012','Favor_2013':'Temporada 2013','Favor_2014':'Temporada 2014','Favor_2015':'Temporada 2015',}, axis = 'columns', inplace=True)

fig, axes = plt.subplots(1, 2)
fig.suptitle('Comparación de goles de local y visitante', fontsize=16)

ax1 = df_local.plot(kind= 'bar',use_index=True,width = 0.85 ,color = ['deeppink','orchid','blueviolet','royalblue'],ax=axes[0],xlabel='Goles de local',fontsize = 10)
ax2 = df_visitante.plot(kind= 'bar',use_index=True,width = 0.85 ,color = ['#003f5c','#7a5195','#ef5675','#ffa600'],ax=axes[1],xlabel ='Goles de visitante')


plt.show()

#--------------------------Grafico 4--------------------------------------
consulta = """
            SELECT DISTINCT home_team_api_id as team_api_id, e.team_long_name as Equipo
            FROM 'enunciado_partidos.csv' AS p
            INNER JOIN 'enunciado_equipos.csv' AS e ON p.home_team_api_id = e.team_api_id
            WHERE (country_id = 13274)
"""
equipos_pais = sql^ consulta

consulta = """
            SELECT DISTINCT p.player_api_id, team_api_id,date,potential,crossing,finishing,dribbling,free_kick_accuracy,ball_control,acceleration,sprint_speed,agility,reactions,balance,shot_power,jumping,strength,aggression,interceptions,vision,penalties,marking                                                                             
            FROM 'pertenece_a.csv' AS p
            INNER JOIN 'enunciado_jugadores_atributos.csv' AS a ON p.player_api_id = a.player_api_id
            WHERE season == '2012/2013'
"""

jugadores2012 = sql^ consulta

consulta1 = """
            SELECT DISTINCT p.player_api_id, team_api_id,date,potential,crossing,finishing,dribbling,free_kick_accuracy,ball_control,acceleration,sprint_speed,agility,reactions,balance,shot_power,jumping,strength,aggression,interceptions,vision,penalties,marking                                                                             
            FROM 'pertenece_a.csv' AS p
            INNER JOIN 'enunciado_jugadores_atributos.csv' AS a ON p.player_api_id = a.player_api_id
            WHERE season == '2013/2014'
"""

jugadores2013 = sql^ consulta1

consulta = """
            SELECT DISTINCT p.player_api_id, team_api_id,date,potential,crossing,finishing,dribbling,free_kick_accuracy,ball_control,acceleration,sprint_speed,agility,reactions,balance,shot_power,jumping,strength,aggression,interceptions,vision,penalties,marking                                                                             
            FROM 'pertenece_a.csv' AS p
            INNER JOIN 'enunciado_jugadores_atributos.csv' AS a ON p.player_api_id = a.player_api_id
            WHERE season == '2014/2015'
"""

jugadores2014 = sql^ consulta

consulta = """
            SELECT DISTINCT p.player_api_id, team_api_id,date,potential,crossing,finishing,dribbling,free_kick_accuracy,ball_control,acceleration,sprint_speed,agility,reactions,balance,shot_power,jumping,strength,aggression,interceptions,vision,penalties,marking                                                                             
            FROM 'pertenece_a.csv' AS p
            INNER JOIN 'enunciado_jugadores_atributos.csv' AS a ON p.player_api_id = a.player_api_id
            WHERE season == '2015/2016'
"""

jugadores2015 = sql^ consulta

#Convierto datetime en solo el año
jugadores2012['date'] = jugadores2012['date'].dt.strftime('%Y')
cols_to_sum = ['potential','crossing','finishing','dribbling','free_kick_accuracy','ball_control','acceleration','sprint_speed','agility','reactions','balance','shot_power','jumping','strength','aggression','interceptions','vision','penalties','marking']
#Creo el la suma de los atributos
jugadores2012['Atributos'] = jugadores2012[cols_to_sum].sum(axis = 1)
#Saco las tablas de atributos individuales que no me importan
jugadores2012 = jugadores2012.drop(cols_to_sum,axis = 1)
#Busco solo los jugadores en 2012, el resto de años esta joineado a la tabla jugadores2012, asi que no son los valores correctos
jugadores2012_ordenados = jugadores2012[jugadores2012['date']=='2012']
#Hago el promedio de todas las mediciones de cada jugador en ese año
jugadores2012_ordenados = jugadores2012_ordenados.groupby(['player_api_id','team_api_id','date']).mean()
jugadores2012_ordenados = jugadores2012_ordenados.droplevel(['player_api_id','date'])
#Hago el promedio de todos los jugadores del mismo equipo
jugadores2012_ordenados = jugadores2012_ordenados.groupby(['team_api_id']).mean()
#Uno la tabla de equipos del pais que tenemos y luego uno con la tabla de cantidad de goles 
ordenados_2012 = jugadores2012_ordenados.merge(equipos_pais,left_index=True,  right_on ='team_api_id',how = 'inner')
ordenados_2012 = ordenados_2012.set_index(['Equipo'])
ordenados_2012 = ordenados_2012.merge(df2012,left_index = True,right_index =True,how = 'inner')
ordenados_2012 = ordenados_2012.droplevel('team_api_id')
ordenados_2012['Goles'] = ordenados_2012['Contra_2012'] + ordenados_2012['Favor_2012']
ordenados_2012 = ordenados_2012.drop(['team_api_id','Contra_2012','Favor_2012'],axis =1)
ordenados_2012 =  ordenados_2012.sort_values(by=['Atributos'])
ordenados_2012['Atributos'] =ordenados_2012['Atributos'].round(decimals=2) 

jugadores2013['date'] = jugadores2013['date'].dt.strftime('%Y')
cols_to_sum = ['potential','crossing','finishing','dribbling','free_kick_accuracy','ball_control','acceleration','sprint_speed','agility','reactions','balance','shot_power','jumping','strength','aggression','interceptions','vision','penalties','marking']
jugadores2013['Atributos'] = jugadores2013[cols_to_sum].sum(axis = 1)
jugadores2013 = jugadores2013.drop(cols_to_sum,axis = 1)
jugadores2013_ordenados = jugadores2013[jugadores2013['date']=='2013']
jugadores2013_ordenados = jugadores2013_ordenados.groupby(['player_api_id','team_api_id','date']).mean()
jugadores2013_ordenados = jugadores2013_ordenados.droplevel(['player_api_id','date'])
jugadores2013_ordenados = jugadores2013_ordenados.groupby(['team_api_id']).mean()
ordenados_2013 = jugadores2013_ordenados.merge(equipos_pais,left_index=True,  right_on ='team_api_id',how = 'inner')
ordenados_2013 = ordenados_2013.set_index(['Equipo'])
ordenados_2013 = ordenados_2013.merge(df2013,left_index = True,right_index =True,how = 'inner')
ordenados_2013 = ordenados_2013.droplevel('team_api_id')
ordenados_2013['Goles'] = ordenados_2013['Contra_2013'] + ordenados_2013['Favor_2013']
ordenados_2013 = ordenados_2013.drop(['team_api_id','Contra_2013','Favor_2013'],axis =1)
ordenados_2013 =  ordenados_2013.sort_values(by=['Atributos'])
ordenados_2013['Atributos'] =ordenados_2013['Atributos'].round(decimals=2) 

jugadores2014['date'] = jugadores2014['date'].dt.strftime('%Y')
cols_to_sum = ['potential','crossing','finishing','dribbling','free_kick_accuracy','ball_control','acceleration','sprint_speed','agility','reactions','balance','shot_power','jumping','strength','aggression','interceptions','vision','penalties','marking']
jugadores2014['Atributos'] = jugadores2014[cols_to_sum].sum(axis = 1)
jugadores2014 = jugadores2014.drop(cols_to_sum,axis = 1)
jugadores2014_ordenados = jugadores2014[jugadores2014['date']=='2014']
jugadores2014_ordenados = jugadores2014_ordenados.groupby(['player_api_id','team_api_id','date']).mean()
jugadores2014_ordenados = jugadores2014_ordenados.droplevel(['player_api_id','date'])
jugadores2014_ordenados = jugadores2014_ordenados.groupby(['team_api_id']).mean()
ordenados_2014 = jugadores2014_ordenados.merge(equipos_pais,left_index=True,  right_on ='team_api_id',how = 'inner')
ordenados_2014 = ordenados_2014.set_index(['Equipo'])
ordenados_2014 = ordenados_2014.merge(df2014,left_index = True,right_index =True,how = 'inner')
ordenados_2014 = ordenados_2014.droplevel('team_api_id')
ordenados_2014['Goles'] = ordenados_2014['Contra_2014'] + ordenados_2014['Favor_2014']
ordenados_2014 = ordenados_2014.drop(['team_api_id','Contra_2014','Favor_2014'],axis =1)
ordenados_2014 =  ordenados_2014.sort_values(by=['Atributos'])
ordenados_2014['Atributos'] =ordenados_2014['Atributos'].round(decimals=2) 

jugadores2015['date'] = jugadores2015['date'].dt.strftime('%Y')
cols_to_sum = ['potential','crossing','finishing','dribbling','free_kick_accuracy','ball_control','acceleration','sprint_speed','agility','reactions','balance','shot_power','jumping','strength','aggression','interceptions','vision','penalties','marking']
jugadores2015['Atributos'] = jugadores2015[cols_to_sum].sum(axis = 1)
jugadores2015 = jugadores2015.drop(cols_to_sum,axis = 1)
jugadores2015_ordenados = jugadores2015[jugadores2015['date']=='2015']
jugadores2015_ordenados = jugadores2015_ordenados.groupby(['player_api_id','team_api_id','date']).mean()
jugadores2015_ordenados = jugadores2015_ordenados.droplevel(['player_api_id','date'])
jugadores2015_ordenados = jugadores2015_ordenados.groupby(['team_api_id']).mean()
ordenados_2015 = jugadores2015_ordenados.merge(equipos_pais,left_index=True,  right_on ='team_api_id',how = 'inner')
ordenados_2015 = ordenados_2015.set_index(['Equipo'])
ordenados_2015 = ordenados_2015.merge(df2015,left_index = True,right_index =True,how = 'inner')
ordenados_2015 = ordenados_2015.droplevel('team_api_id')
ordenados_2015['Goles'] = ordenados_2015['Contra_2015'] + ordenados_2015['Favor_2015']
ordenados_2015 = ordenados_2015.drop(['team_api_id','Contra_2015','Favor_2015'],axis =1)
ordenados_2015 =  ordenados_2015.sort_values(by=['Atributos'])
ordenados_2015['Atributos'] =ordenados_2015['Atributos'].round(decimals=2) 


ordenados_2012 = ordenados_2012.reset_index()
ordenado2012 = pd.melt(ordenados_2012,id_vars=["Equipo"],value_vars=["Atributos","Goles"],var_name="Indice",ignore_index=False)

ordenados_2013 = ordenados_2013.reset_index()
ordenado2013 = pd.melt(ordenados_2013,id_vars=["Equipo"],value_vars=["Atributos","Goles"],var_name="Indice",ignore_index=False)

ordenados_2014 = ordenados_2014.reset_index()
ordenado2014 = pd.melt(ordenados_2014,id_vars=["Equipo"],value_vars=["Atributos","Goles"],var_name="Indice",ignore_index=False)

ordenados_2015 = ordenados_2012.reset_index()
ordenados_2015 = pd.melt(ordenados_2015,id_vars=["Equipo"],value_vars=["Atributos","Goles"],var_name="Indice",ignore_index=False)


fig,ax = plt.subplots()
fig.suptitle('Comparación de goles por la suma de atributos de cada equipo temporada 2012' , fontsize=16)
p = sns.barplot(x="value", y="Equipo", hue="Indice", data=ordenado2012, palette=["steelblue","coral"], saturation=1)
p.set(xlabel="Atributos/Goles", ylabel="Equipos")

fig,ax = plt.subplots()
fig.suptitle('Comparación de goles por la suma de atributos de cada equipo temporada 2013' , fontsize=16)
p = sns.barplot(x="value", y="Equipo", hue="Indice", data=ordenado2013, palette=["steelblue","coral"], saturation=1)
p.set(xlabel="Atributos/Goles", ylabel="Equipos")

fig,ax = plt.subplots()
fig.suptitle('Comparación de goles por la suma de atributos de cada equipo temporada 2014' , fontsize=16)
p = sns.barplot(x="value", y="Equipo", hue="Indice", data=ordenado2014, palette=["steelblue","coral"], saturation=1)
p.set(xlabel="Atributos/Goles", ylabel="Equipos")

fig,ax = plt.subplots()
fig.suptitle('Comparación de goles por la suma de atributos de cada equipo temporada 2015' , fontsize=16)
p = sns.barplot(x="value", y="Equipo", hue="Indice", data=ordenados_2015, palette=["steelblue","coral"], saturation=1)
p.set(xlabel="Atributos/Goles", ylabel="Equipos")






