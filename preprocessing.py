import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.model_selection import StandardScaler
df = pd.DataFrame({
    "Math": [80, 60, None, 90, 70],
    "English": [75, None, 65, 85, 60],
    "Science": [70, 55, 60, None, 65],
    "Gender": ["Male", "Female", "Male", "Female", None],
    "Result": ["Pass", "Fail", "Fail", "Pass", "Pass"]
})

# print(df.info())
# print(df.isnull().sum)
df["Math"].fillna(df["Math"].mean(),inplace= True)
df["English"].fillna(df["English"].mean(),inplace=True)
df["Science"].fillna(df["Science"].mean(),inplace=True)
df["Gender"].fillna(df["Gender"].mode()[0],inplace=True)



df["Gender"] = df["Gender"].map({
    "Male": 0,
    "Female": 1
})

df["Result"] = df["Result"].map({
    "Pass" : 1,
    "Fail": 0
})

X = df.drop("Result",axis=1)
y = df.drop("Result")


X_train, X_test, y_train, y_test = train_test_split(
    X,y
    test_size = 0.2,
    random_state=42
)

scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_train)