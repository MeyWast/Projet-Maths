# import librairies
import pandas as pd
import pylab as pl
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

# Noms des donnes
donnees = ["Instant", "Latitude", "Longitude", "Pays", "Magnitude", "Profondeur"]

# import data
data = pd.read_csv('seismes_2014.csv', names = donnees, skiprows = 1)

# Afficher les premières lignes du DataFrame
# print(data)

# Donner le nombre total de séismes enregistrés en 2014. 
# print("nombre de séisme :", data.shape[0])

# afficher le pays avec le plus de séisme 
# print("pays avec le plus de séisme :", data["Pays"].value_counts().head(20))

# Construire un code permettant d’obtenir la table des effectis des 20 lieux les plus fréquemment secoués dans le monde. 
# noms = data["Pays"].value_counts().head(20).index.tolist()

# Pour chacun de ces 20 lieux et pour la variable mag, représenter la boîte à moustaches.
# magnitudes = []

# for lieu in noms:
#     mag = data[data["Pays"] == lieu]["Magnitude"].tolist()
#     magnitudes.append(mag)

# plt.xlabel("Pays")
# plt.ylabel("Magnitude")

# sns.boxplot(data=magnitudes, whis=[0,100])
# plt.xticks(range(len(noms)), noms, rotation=90)
# plt.show()

# Donner les 6 lieux du monde qui enregistrent les plus fortes magnitudes. 
# max_mag = data.groupby("Pays")["Magnitude"].max().nlargest(6)
# pays = data[data["Pays"].isin(max_mag.index)]["Pays"].unique()
# print(pays)

# Pour la Californie et l’Alaska, donner le nombre de séismes de magnitude inférieure ou égale à 2.
# California = data[(data["Pays"] == "California") & (data["Magnitude"] <= 2)].shape[0]
# Alaska = data[(data["Pays"] == "Alaska") & (data["Magnitude"] <= 2)].shape[0]

# print("Nombre de micros-tremblement en Californie", California)
# print("Nombre de micros-tremblement en Alaska", Alaska)

# Sélection des séismes perceptibles pour l’humain 
# F = data[(data["Magnitude"] >= 5) & (data["Magnitude"] <= 8)]
# F = data[(data["Magnitude"] >= 3) & (data["Magnitude"] < 5)]
# F['m'] = F['Magnitude'].astype(int)
# F['Taille'] = 10 + 10 * (F['m'] - 5)

# Définir votre clé Mapbox
# mapbox_token = 'pk.eyJ1IjoibGVuZHJheGFlIiwiYSI6ImNsaWNzejlldjBmM2UzZ21xYm53NmNyODEifQ.FQ7qiYDTh-RSKyvlYYI69Q'

# Dictionnaire de la palette de couleurs
# palette = {
#     3: 'hotpink',
#     4: 'green',
#     5: 'chocolate',
#     6: 'blue',
#     7: 'red',
#     8: 'black'
# }

# Créer la carte de chaleur des séismes de magnitude inférieure à 5 avec votre palette de couleurs personnalisée
# fig = px.density_mapbox(F, lat='Latitude', lon='Longitude', z='Magnitude', radius=3,
#                          center=dict(lat=0, lon=180), zoom=0,
#                          mapbox_style="stamen-terrain")

# fig = px.density_mapbox(F, lat='Latitude', lon='Longitude', z='Magnitude', radius=F['Taille'].tolist(),
#                         center=dict(lat=0, lon=180), zoom=0,
#                         mapbox_style="stamen-terrain", color_continuous_scale=list(palette.values()))

# Afficher la carte
# fig.show()

E = data[(data["Magnitude"] >= 5) & (data["Magnitude"] <= 8)]
E['m'] = E['Magnitude'].astype(int) 
E['Taille'] = 10 + 10 * (E['m']- 5)
mapbox_token = 'pk.eyJ1IjoibGVuZHJheGFlIiwiYSI6ImNsaWNzejlldjBmM2UzZ21xYm53NmNyODEifQ.FQ7qiYDTh-RSKyvlYYI69Q'
palette = {
    3: 'hotpink',
    4: 'green',
    5: 'chocolate',
    6: 'blue',
    7: 'red',
    8: 'black'
}

fig = px.density_mapbox(E, lat='Latitude', lon='Longitude', z='Magnitude', radius=E['Taille'].tolist(),
                        center=dict(lat=0, lon=180), zoom=0, mapbox_style="dark", color_continuous_scale=list(palette.values()))

# Afficher la carte
fig.show()



