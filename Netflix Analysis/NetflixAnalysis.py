import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv("Dataset/netflix_titles.csv")
print(data.shape)
print("-----")
print(data.head())
print("-----")
print(data.columns)
print("-----")
print(data.info)
print("-----")
print(data.info())
print("-----")
print(data.describe(include="all"))
print("-----")
print(data.isna().sum())
print("-----")
print(data["director"])
print("-----")
print(len(data["director"]))
print("-----")
print(data[data["director"] == "Mana Yasuda"])
print("-----")
print(len(data[data["director"] == "Mana Yasuda"]))
print("-----")

print("What is the percentage of movies and tv shows available in Netflix?")
showType = data["type"]
print(showType)
perMovies = len(data[data["type"] == "Movie"])/len(data) * 100
perShows = len(data[data["type"] == "TV Show"])/len(data) * 100
print(perMovies)
print(perShows)
labels = "Movies", "TV Shows"
sizes = [perMovies, perShows]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, explode=(0,0.1))
plt.show()

