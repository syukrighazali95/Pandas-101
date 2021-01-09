import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from itertools import chain
from collections import Counter
import seaborn as sns

li = [10, 20, 30, 40, 50]
s = pd.Series






#########################################################

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

############################################################

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
ax1.set_title("Percentage of movies and tv shows in Netflix")
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, explode=(0,0.1))
# plt.show()
print("-----")

##############################################################

print("What are the top 10 categories in Netflix?")
category = data["listed_in"].str.split(",")
print(category)
category = data["listed_in"].str.split(",",expand=True)
print(category)

# Removing whitespaces in categories
for col in category.columns:
    category[col] = category[col].str.strip()
category_df = pd.DataFrame(category)
# print(category_df.values.tolist())
category_list = []

# Removing None in the list
for i in category_df.values.tolist():
    li = []
    for item in i:
        if item != None:
            li.append(item)
    category_list.append(li)
# print(category_list)
# Combine or chain lists into one list
category_chain = chain.from_iterable(category_list)
# Return tuple of count for each category 
category_count = Counter(category_chain)
print(category_count)

# Most common categories
common_categories = dict(category_count.most_common(10))
key = list(common_categories.keys())
value = list(common_categories.values())

# Plot the graph
plt.figure(figsize = (10,7))
plt.title("Top 10 most common categories for TV Shows and Movies in Netflix")
plt.xticks(rotation = 45)
plt.xlabel("Categories")
plt.ylabel("Number of shows")
plt.bar(key, value, color='blue')
# plt.show()

##############################################################

print("Distribution of Netflix Movies in minutes")
duration_list = []
for item in data["duration"]:
    tmp = item.split()
    # print(tmp[1])
    if tmp[1] == "min":
        duration_list.append(int(item.strip("min")))
# print(duration_list)
distribution = pd.DataFrame(duration_list)

plt.figure(figsize=(15,7))
sns.distplot(distribution, color='red')
plt.title("Distribution of Netflix Movies Duration in minutes")
plt.xlabel('Duration')

distribution.hist(column=0, bins=30, grid=False, alpha=0.7, edgecolor="black")
plt.title("Histogram of Netflix Movies Duration in minutes")
plt.xlabel('Duration in mins')
plt.show()

##############################################################