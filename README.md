# 🐍 Python to ML Foundation

This repository documents my **daily learning journey of Python fundamentals, NumPy, and Pandas**, with the goal of building a **strong foundation before starting Machine Learning**.

Instead of rushing into ML algorithms, this repo focuses on **thinking clearly, understanding code behavior, and handling data properly**.

---

## 🎯 Purpose of This Repository

Machine Learning is not just about models and formulas.  
It heavily depends on:

- Strong Python logic
- Clean and readable code
- Comfortable data handling
- Understanding *why* code behaves the way it does

This repository exists to strengthen those skills step by step.

---

## 📘 What I’m Learning Here

### 🔹 Core Python
- Conditions & loops
- Membership and logical operators
- Functions (default args, `*args`, `**kwargs`)
- Lambda expressions
- List comprehensions
- Dictionaries, sets, tuples
- File handling & JSON
- Object-Oriented Programming (OOPs)

### 🔹 NumPy
- Arrays & dimensions
- Indexing and slicing
- Reshaping
- Mathematical operations
- Iteration techniques

### 🔹 Pandas
- Series & DataFrames
- Data selection (`loc`, `iloc`)
- Filtering & conditions
- Handling missing values
- Sorting & grouping
- Basic exploratory data analysis (EDA)

---
📊 Matplotlib for AI-ML, Deep Learning & GenAI

This repository contains a focused and practical guide to Matplotlib, covering only those concepts that are required for AI, Machine Learning, Deep Learning, and Generative AI workflows.

🎯 Goal:
Learn how to visualize data, understand patterns, detect issues, and analyze model performance — not decorative plotting.

🚀 Why Matplotlib for ML?

In real-world ML projects:

Models don’t fail because of algorithms

They fail because data is misunderstood

Matplotlib helps you:

Perform Exploratory Data Analysis (EDA)

Detect outliers & class imbalance

Visualize training & validation performance

Explain results clearly in reports & notebooks

🧠 What You Will Learn (ML-Focused Only)
1️⃣ Matplotlib Basics

Importing Matplotlib

Creating basic figures

Displaying plots

import matplotlib.pyplot as plt

2️⃣ Line Plots (Most Important)

Use cases:

Training loss vs epochs

Validation loss vs epochs

Accuracy curves

plt.plot(epochs, loss)
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("Training Loss Curve")
plt.show()


📌 Used heavily in Deep Learning.

3️⃣ Multiple Line Plots (Model Comparison)

Use cases:

Train vs Validation loss

Overfitting detection

plt.plot(train_loss, label="Train Loss")
plt.plot(val_loss, label="Validation Loss")
plt.legend()
plt.show()

4️⃣ Scatter Plots

Use cases:

Feature relationships

Outlier detection

Cluster visualization

plt.scatter(df["Age"], df["Salary"])
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()

5️⃣ Histogram (Data Distribution)

Use cases:

Normality check

Skewness analysis

Scaling decisions

plt.hist(df["Age"], bins=20)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

6️⃣ Bar Charts (Categorical Data)

Use cases:

Class imbalance detection

Category frequency

plt.bar(categories, values)
plt.show()

7️⃣ Labels, Titles & Legends (Mandatory)

Clear graphs are critical for:

Reports

Interviews

Model explanations

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Plot Title")
plt.legend()

8️⃣ Figure Size & Grid

Improves readability for large datasets.

plt.figure(figsize=(8,5))
plt.grid(True)

9️⃣ Subplots (Comparative Analysis)

Use cases:

Before vs after preprocessing

Feature comparison

plt.subplot(1,2,1)
plt.hist(df["Age"])

plt.subplot(1,2,2)
plt.hist(df["Salary"])
plt.show()

🔟 Saving Plots

Useful for:

Reports

GitHub projects

Documentation

plt.savefig("loss_curve.png")

❌ What This Repo Does NOT Cover (Intentionally)

These topics are not required for ML/DL/GenAI:

3D plots

Animations

Advanced styling

GUI interactions

Custom backends

⛔ Focus is on insight, not decoration.

## 🧠 Learning Style

Each topic is learned using:
- Small and clear code snippets
- Output-prediction based examples
- Edge cases that improve logical thinking
- Simple explanations in a human way

Many examples are intentionally **slightly tricky** to improve understanding instead of memorization.

---

## 📂 Repository Structure