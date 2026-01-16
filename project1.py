import pandas as pd #table data handle krne ke liye
import numpy as np  #no. and arrays ke liye
import matplotlib.pyplot as plt #graph and plots banane ke liye
import seaborn as sns #advanced beautiful plot banane ke liye
import warnings as wr #unnecessary warnings hide krne ke liye
wr.filterwarnings('default')

#READING DATASET

df = pd.read_csv('WineQT.csv') #comma seperated values
print(df);

#ANALYZING 
print(df.head()) #top 5 values
print(type(df.shape)) #shape tuple hai 
print(df.shape) #(rows,col) #data kitna hai check krne ke liye
#rows are observation and col are features

print(df.info()) #checks if any values are missing and memory usage

print(df.describe()) #mean std deviation and quartiles etc ye sab deta hai 

print(df.columns.tolist()) #col ko list mein convert krne ke liye


#CHECKING MISSING VALUES
print(df.isnull().sum()) #returns total no of null values per cols

#CHECK FOR DUPLICATES
print(df.nunique()) #no. of unique values per cols

#UNIVARIATE ANALYSIS
#observation consist only one varible 

quality_counts = df['quality'].value_counts()
print(quality_counts) #har unique value kitni baar ayi hai 


plt.figure(figsize=(8,6))
plt.bar(quality_counts.index,quality_counts,color='deeppink')
#quality_counts mein (index,values hoti hain) lekin matplot lib bs values uthata hai  

plt.title('Count plot of quality')
plt.xlabel('Quality')
plt.ylabel('Count')
# plt.show()

#  Kernel density plot for understanding variance in the dataset
#low variance data kitna chipka hai 
#high variance data kitna door hai

sns.set_style('darkgrid')
numerical_cols = df.select_dtypes(include=['int64','float64']).columns #sirf numerical cols select krne ke liye

plt.figure(figsize=(14,len(numerical_cols)*3)) #inches

for idx, feature in enumerate(numerical_cols,1):
    plt.subplot(len(numerical_cols),3,idx) #subplots(nrow,ncol,position) ye rxc ka grid banataa aur idx se start hota hai 
    #subplot layout decide krta hai 
    sns.histplot(df[feature],kde=True) #hisplot data plot krta hai ::::: KDE ek smooth curve hota hai jo data ka distribution dikhata hai
    plt.title(f'{feature} | Skewness: {round(df[feature].skew(),2)}') #skewness mtalb data kitna jhuka hua hai 2 decimal places tak skewness value calculate krni hai

plt.tight_layout() #subplots ke bich adjust krne ke liye
# plt.show()


# Swarm Plot for showing the outlier in the data
# Swarm plot categorical vs numerical data ka distribution dikhata hai jahan har data point visible hota hai, isliye outliers easily detect hote hain.

plt.figure(figsize=(10,8))
sns.swarmplot(x='quality',y='alcohol',data=df,palette='viridis')
plt.title('Swarm plot for Quality and Alcohol')
plt.xlabel('Quality')
plt.ylabel('Alcohol')
# plt.show()





#BIVARIATE ANAYLSIS
#do variables ke bich pattern, dependency, aur relationship check krna
#how changes in one variable affect the other variable



# Pair Plot for showing the distribution of the individual variables
important_cols = [
    'alcohol',
    'quality',
    'volatile acidity',
    'density',
    'pH'
]

sns.set_palette('Pastel1')
plt.figure(figsize=(8,4))
sns.pairplot(df[important_cols])
#pair all vs all ka graph plot krta hai 
plt.suptitle('Pair plot for Dataframe')
plt.show()

#histogram jo isme hote hain vo single variable ka distribution dikhate hain
#scatterplot offdiagonal b/w two var reaveals pattern and corelation

