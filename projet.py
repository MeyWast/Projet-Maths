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

# fig = px.scatter_mapbox(E, lat='Latitude', lon='Longitude', size='Taille', color='m', 
#                  color_continuous_scale=list(palette.values()), center=dict(lat=0, lon=180), zoom=0)

# fig.update_layout(mapbox_style="streets", mapbox_accesstoken=mapbox_token)
# Afficher la carte
# fig.show()

# import plotly.graph_objects as go

# E = data[(data["Magnitude"] >= 3) & (data["Magnitude"] < 9)]
# E['m'] = E['Magnitude'].astype(int)
# E['Taille'] = 5 + 5 * (E['m'] - 2)
# m3 = E[E['m'] == 3]
# m4 = E[E['m'] == 4]
# m5 = E[E['m'] == 5]
# m6 = E[E['m'] == 6]
# m7 = E[E['m'] == 7]
# m8 = E[E['m'] == 8]

# # Données des marqueurs
# lats = E['Latitude'].tolist()
# lons = E['Longitude'].tolist()
# sizes = E['Taille'].tolist()

# # Dictionnaire de correspondance des valeurs de m avec les couleurs
# palette = {
#     3: 'hotpink',
#     4: 'green',
#     5: 'chocolate',
#     6: 'blue',
#     7: 'red',
#     8: 'black'
# }

# # Création de la liste de couleurs en fonction des valeurs de m
# couleurs = [palette[m] for m in E['m']]

# hover_text = [
#     f"Date: {date}<br>Latitude: {lat}<br>Longitude: {lon}<br>Magnitude: {size}<br>Lieu: {pays}"
#     for date, lat, lon, size, pays in zip(E['Instant'], E['Latitude'], E['Longitude'], E['m'], E['Pays'])
# ]

# # Création de la trace Scattergeo avec les marqueurs, les couleurs et le texte de survol
# trace = go.Scattergeo(
#     lat=lats,
#     lon=lons,
#     mode='markers',
#     marker=dict(
#         size=sizes,
#         color=couleurs,
#         line=dict(width=0.5, color='white')
#     ),
#     hovertemplate="<b>%{text}</b><extra></extra>",  # Utilisation de la variable de texte
#     text=hover_text,  # Assignation du texte de survol à la variable de texte
#     legendgroup='markers',  # Assignation du même legendgroup pour le trace principal
#     name="Magnitude m"
# )

# fig = go.Figure()


# fig.add_trace(trace)

# # Répartition des valeurs de m
# labels = [len(m3), len(m4), len(m5), len(m6), len(m7), len(m8)]
# values = [len(m3), len(m4), len(m5), len(m6), len(m7), len(m8)]

# # Création de la trace de camembert en légende
# pie_trace = go.Pie(
#     labels=labels,
#     values=values,
#     marker=dict(colors=[palette[m] for m in range(3, 9)]),
#     domain={'x': [0, 0.4], 'y': [0.8, 1]},
#     name='Magnitude Distribution',
#     legendgroup='magnitude'
# )

# fig.add_trace(pie_trace)
# for i in range(3, 9):
#     # Création d'une trace Scattergeo pour chaque valeur de m
#     trace_temp = go.Scattergeo(
#         lat=E[E['m'] == i]['Latitude'],
#         lon=E[E['m'] == i]['Longitude'],
#         mode='markers',
#         marker=dict(
#             size=5 + 5 * (i - 2),
#             color=['hotpink', 'green', 'chocolate', 'blue', 'red', 'black'][i - 3],
#             line=dict(width=0.5, color='white')
#         ),
#         hoverinfo='none',  # Pas de texte de survol
#         name="m = " + str(i)
#     )
#     fig.add_trace(trace_temp)  # Ajout de la trace à la figure




# fig.update_geos(projection_type="natural earth")
# fig.update_layout(
#     height=500,
#     margin={"r": 0, "t": 0, "l": 0, "b": 0},
#     dragmode=False
# )

# fig.show()
