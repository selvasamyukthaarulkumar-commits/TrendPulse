import pandas as pd
import numpy as np

print("Starting Task 3 - Data Analysis")

# -------------------------------
# STEP 1: Load CSV
# -------------------------------

file_path = "data/trends_clean.csv"

df = pd.read_csv(file_path)
df.columns = df.columns.str.strip()
print("columns:",df.columns)

print("Data loaded successfully")

# print first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# print shape
print("\nShape of data (rows, columns):", df.shape)

# average score and comments
print("\nAverage score:", df["score"].mean())
print("Average comments:", df["num_comments"].mean())

# -------------------------------
# STEP 2: Basic Analysis (NumPy)
# -------------------------------

print("\n--- Basic Analysis Numpy stats ---")

scores = df["score"].values
comments = df["num_comments"].values


# mean
print("Mean score:", np.mean(scores))
print("Mean comments:", np.mean(comments))


# median
print("Median score:", np.median(scores))

# standard deviation
print("Score standard deviation:", np.std(scores))

# highest and lowest score
print("Highest score:", np.max(scores))
print("Lowest score:", np.min(scores))

# most commented story
max_comments = np.max(comments)

row = df[df["num_comments"] == max_comments].iloc[0]

print("\nStory with most comments:")
print("Title:", row["title"])
print("Comments:", row["num_comments"])


# -------------------------------
# STEP 3: Add new columns
# -------------------------------

#1 Engagement = num-comments/ (score + 1)
df["engagement"] = df["num_comments"] / (df["score"] + 1)
 #2 is_popular 
avg_score = df["score"].mean()
df["is_popular"] = df["score"] > avg_score
print("\nNew column 'is_popular' added ")


# -------------------------------
# STEP 4: Save new CSV
# -------------------------------

output_path = "data/trends_analysis.csv"

df.to_csv(output_path, index=False)

print("\nNew CSV saved successfully")

