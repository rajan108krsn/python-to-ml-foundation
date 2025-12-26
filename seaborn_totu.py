import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# sns.histplot([1,2,3,4,5], kde=True)
# plt.show()

df = pd.read_csv("students.csv")

# sns.scatterplot(
#     data=df,
#     x="Age",
#     y="Marks",
#     hue="City"
# )
# plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# df = pd.DataFrame({
#     "Salary": [10000, 12000, 13000, 14000, 15000, 16000, 100000]
# })

# sns.boxplot(x=df["Salary"])
# df = pd.DataFrame({
#     "Gender": ['Male','Female','Male']
# })
# sns.countplot(x=df["Gender"])


df = pd.DataFrame({
    "Age": [20, 25, 30, 35, 40],
    "Salary": [20000, 30000, 50000, 60000, 80000],
    "Marks": [60, 65, 70, 75, 80]
})
corr = df.corr()
sns.heatmap(corr,annot=True)
plt.show()

