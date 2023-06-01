# import librairies
import pandas as pd
import pylab as pl
import seaborn as sns
import matplotlib.pyplot as plt


# Noms des donnes
donnees = ["Instant", "Latitude", "Longitude", "Pays", "Magnitude", "Profondeur"]

# import data
data = pd.read_csv('seismes_2014.csv', names = donnees, skiprows = 1)

# Afficher les premières lignes du DataFrame
# print(data)

# afficher les lignes de data
# print("nombre de séisme :", data.shape[0])

# afficher le pays avec le plus de séisme 
# print("pays avec le plus de séisme :", data["Pays"].value_counts().head(20))

Pays = data["Pays"].value_counts().head(20).index.tolist()
data_frame = []

for lieu in Pays:
    data_frame.append(data[data["Pays"] == lieu]["Magnitude"].tolist())
    

plt.boxplot(data_frame)

plt.ylim(0,10)

pylab.xticks(Pays)

plt.show()