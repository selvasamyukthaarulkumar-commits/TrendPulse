import pandas as pd
import matplotlib.pyplot as plt
import os

# read csv
df = pd.read_csv("data/trends_analysis.csv")

# create folder
if not os.path.exists("outputs"):
    os.mkdir("outputs")

# ---------------- Chart 1 ----------------
top = df.sort_values("score", ascending=False).head(10)

titles = top["title"].str[:50]
scores = top["score"]

plt.figure()
plt.barh(titles, scores)
plt.title("Top 10 Stories by Score")
plt.xlabel("Score")
plt.ylabel("Stories")
plt.gca().invert_yaxis()
plt.savefig("outputs/chart1_top_stories.png")
plt.close()


# ---------------- Chart 2 ----------------
cat = df["category"].value_counts()

plt.figure()
plt.bar(cat.index, cat.values)
plt.title("Stories per Category")
plt.xlabel("Category")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.savefig("outputs/chart2_categories.png")
plt.close()


# ---------------- Chart 3 ----------------
pop = df[df["is_popular"] == True]
not_pop = df[df["is_popular"] == False]

plt.figure()
plt.scatter(pop["score"], pop["num_comments"], label="Popular")
plt.scatter(not_pop["score"], not_pop["num_comments"], label="Not Popular")

plt.title("Score vs Comments")
plt.xlabel("Score")
plt.ylabel("Comments")
plt.legend()
plt.savefig("outputs/chart3_scatter.png")
plt.close()