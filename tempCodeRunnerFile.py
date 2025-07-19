typecount=df["type"].value_counts()
# plt.figure(figsize=(8,6))
# plt.bar(typecount.index,typecount.values,color=["orange","blue"])
# plt.xlabel("Type")
# plt.ylabel("count")
# plt.title("Number of movies and Tv shows on netflix")
# plt.tight_layout()
# plt.savefig("movies vs tvshows.png")
# plt.show()

# ratings=df["rating"].value_counts()
# plt.figure(figsize=(8,6))
# plt.pie(ratings,labels=ratings.index,autopct="%1.1f%%")
# plt.title("Percentage of content ratings")
# plt.tight_layout()
# plt.savefig("percentage content rating.png")
# plt.show()

# movies=df[df["type"]=="Movie"].copy()
# movies["duration_int"] = pd.to_numeric(
#     movies["duration"].str.replace("min", "", regex=False).str.strip(),
#     errors="coerce"
# ).astype("Int64")
# plt.figure(figsize=(8,6))
# plt.hist(movies["duration_int"],bins=30,color="skyblue",edgecolor="black")
# plt.xlabel("Duration (minutes)")
# plt.ylabel("Number of movies")
# plt.title("Duration of movies")

# plt.tight_layout()
# plt.savefig("durationmovies.png")
# plt.show()


# realse=df["release_year"].value_counts().sort_index()
# plt.figure(figsize=(8,6))
# plt.scatter(realse.index,realse.values,color="red")
# plt.xlabel("Number of shows")
# plt.ylabel("Years")
# plt.title("release year vs shows")
# plt.grid(linewidth=1)
# plt.tight_layout()
# plt.savefig("releaseeyear scatter.png")
# plt.show()