import pandas as pd

print("Starting Task 2 - Data Cleaning Process")

# -------------------------------
# STEP 1: Load the JSON file
# -------------------------------

# JSON file path (change date if needed)
file_path = "data/trends_20260406.json"

# Read JSON file into DataFrame
df = pd.read_json(file_path)
print(df.columns)

print("Total rows loaded from JSON file:", len(df))



# -------------------------------
# STEP 2: Clean the Data
# -------------------------------

# 1. Remove duplicate stories based on post_id
duplicates = df.drop_duplicates(subset="post_id").sum()
print("Duplicates rows:",duplicates)
#count missing values
missing = df.isnull().sum()
print("Missing values:\n" , missing)
# 2. Remove rows where important values are missing
df = df.dropna(subset=["post_id", "title", "score"])
print("Missing values removed")

# 3. Convert score and num_comments to integer
df["score"] = df["score"].astype(int)

# Some rows may have missing comments, so fill with 0
if "num_comments" in df.columns : 
    df["num_comments"]=df["num_comments"].fillna(0).astype(int)

print("Data types corrected")

# 4. Remove low quality posts (score less than 5)
before_count = len(df)
df = df[df["score"] >= 5]
after_count = len(df)
removed = before_count - after_count
print("Low score posts removed:",removed)


# 5. Clean extra spaces in title
df["title"] = df["title"].str.strip()
print("Title cleaned")

# Final row count after cleaning
print("Rows remaining after cleaning:", len(df))


# -------------------------------
# STEP 3: Save as CSV
# -------------------------------

output_path = "data/trends_clean.csv"

# Save cleaned data to CSV file
df.to_csv(output_path, index=False)

print("Cleaned data saved as CSV file successfully")


# -------------------------------
# STEP 4: Summary
# -------------------------------

print("\nSummary of stories by category:")

# Count how many stories in each category
category_count = df["category"].value_counts()

print(category_count)

