import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("netflix_titles.csv")
#print(df.head())
#print(df.columns)

df.dropna(subset=["type","release_year","duration","rating","country"])
print(df.duplicated().sum())

typecount=df["type"].value_counts()
plt.figure(figsize=(8,6))
plt.bar(typecount.index,typecount.values,color=["orange","blue"])
plt.xlabel("Type")
plt.ylabel("count")
plt.title("Number of movies and Tv shows on netflix")
plt.tight_layout()
plt.savefig("movies vs tvshows.png")
plt.show()

ratings=df["rating"].value_counts()
plt.figure(figsize=(8,6))
plt.pie(ratings,labels=ratings.index,autopct="%1.1f%%")
plt.title("Percentage of content ratings")
plt.tight_layout()
plt.savefig("percentage content rating.png")
plt.show()

movies=df[df["type"]=="Movie"].copy()
movies["duration_int"] = pd.to_numeric(
    movies["duration"].str.replace("min", "", regex=False).str.strip(),
    errors="coerce"
).astype("Int64")
plt.figure(figsize=(8,6))
plt.hist(movies["duration_int"],bins=30,color="skyblue",edgecolor="black")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of movies")
plt.title("Duration of movies")

plt.tight_layout()
plt.savefig("durationmovies.png")
plt.show()


realse=df["release_year"].value_counts().sort_index()
plt.figure(figsize=(8,6))
plt.scatter(realse.index,realse.values,color="red")
plt.xlabel("Number of shows")
plt.ylabel("Years")
plt.title("release year vs shows")
plt.grid(linewidth=1)
plt.tight_layout()
plt.savefig("releaseeyear scatter.png")
plt.show()

countries=df["country"].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(countries.index,countries.values,color="Purple")
plt.xlabel("Number of shows")
plt.ylabel("Countries")
plt.title("Top 10 countries by number of shows")
plt.tight_layout()
plt.savefig("top10 countries.png")
plt.show()

content_byyear=df.groupby(["release_year","type"]).size().unstack().fillna(0)

fig, ax=plt.subplots(1, 2, figsize=(12,6))

ax[0].plot(content_byyear.index, content_byyear["Movie"], color="green")
ax[0].set_title("Movies Released per year")
ax[0].set_xlabel("Year")
ax[0].set_ylabel("Number of Movies")

ax[1].plot(content_byyear.index, content_byyear["TV Show"], color="brown")
ax[1].set_title("Tv show Released per year")
ax[1].set_xlabel("Year")
ax[1].set_ylabel("Number of Tv shows")

fig.suptitle("Comparsion of Movies and Tv shows over the years")
plt.savefig("Comparsion of Movies and Tv shows over the year")
plt.tight_layout()

plt.show()