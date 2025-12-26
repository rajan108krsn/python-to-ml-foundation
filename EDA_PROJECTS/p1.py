import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Goal:

# Students ke marks, age, gender ka analysis

# Ye samajhna:

# Kaun better perform kar raha hai?

# Kya age / gender ka impact hai?

# Pass / Fail patterns kya hain?

# 📌 Interview line:

# “This EDA helps in understanding data distribution and feature relevance before applying ML models.”


df = pd.read_csv("std.csv")

# First Look at Data
# print(df.shape)
# print(df.info)
# ?print(df.describe)

# Data Cleaning
# print(df.isnull().sum())

#agr missing hoto
# df.fillna(df.mean(numeric_only=True),inplace=True)

#drop duplicates
# df.drop_duplicates(inplace=True)

# Feature Engineering

df["Total Marks"] = df["English"] + df["Science"] + df["Math"]
df["Average Marks"] = df["Total Marks"]/3

df["Result"] = df["Average Marks"].apply(
    lambda x: "Pass" if x >= 0 else  "Fail"
)
print(df)

# plt.hist(df['Average Marks'],bins=10)
# plt.title("Average Marks Distribution")
# plt.show()

# sns.countplot(x="Result", data = df)
# plt.show()

# sns.boxplot(x="Gender",y="Average Marks", data = df)
# plt.title("Gender vs Performance")
# plt.show()

# sns.scatterplot(x="Age", y="Average Marks", data=df)
# plt.title("Age vs Average Marks")
# plt.show()


corr = df[["Math", "English", "Science", "Average Marks"]].corr()
sns.heatmap(corr,annot=True)
plt.title("Subject Correlation")
plt.show()