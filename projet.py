# import librairies
import pandas as pd
import pylab as pl
import seaborn as sns

# Noms des donnes
donnees = ["Instant", "Latitude", "Longitude", "Pays", "Magnitude", "Profondeur"]

# import data
data = pd.read_csv('seismes_2014.csv', names = donnees, skiprows = 1)

# Afficher les premières lignes du DataFrame
# print(data)

# afficher les lignes de data
print(data.shape[0])
