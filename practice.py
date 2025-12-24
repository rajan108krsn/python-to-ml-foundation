# print("p" in "python")
# print(5 in [1,2,3,4])
# print("Hare Krishna")

# age = 18
# if age > 18:
#     print("You are eligible to vote.")
# elif age == 18:
#     print("Just 18")
# else:
#     print("You are not eligible to vote.")

# x=9

# if x>0:
#     if x<10:
        # print("x is a positive single-digit number.")

# for i in range(5) :
#     print(i)
# i =0
# while i < 5:
#     print(i)
#     i += 1

# for i in range(5):
#     print(i)
# else:
#     print("Hari bol")

# for i in range(1,2,8):
#     if(i==7):
#         break
# else:
#     print("Hare Krishna")

# def radheradhe():
#     print("Radhe Radhe")
# radheradhe()

# def add(a,b):
#     return a+b
# print(add(3,5))

# def info (name="Krishna"):
#     print("Name is", name)
 
# info("Radhe")
# info()

# def inf(name1,name2):
#     print(name1,name2)
# inf(name2="Shyam",name1="Madhav")
# inf("Madhav","Shyam")

# def sum_all(*args):    
#     return sum(args)
# print(sum_all(1,2,3,4,5))

# def detailes(**data):
#     print(data)
# detailes(name="Krishna",age=18,city="Vrindavan")

#Lambda Function
# x = lambda a, b : a + b
# print(x(5,10))
# y = lambda a : a+10
# print(y(2))

# cube = lambda x : x*x*x
# print(cube(3))

# square = lambda x : x*x
# print("The square is", square(4))

# even = lambda x: "Even" if x%2 ==0 else "Odd"
# print(even(5))

# greater = lambda a, b: a if a > b else b
# print(greater(10,5))

# students = [("Krishan",16),("Radha",15),("Gopal",17)]
# students.sort(key=lambda x: x[0])
# print(students)

# numbers = [1,4,3,2,2]
# result = list(map(lambda x: x*x, numbers))
# print(result)

# num = [4,3,5,4]
# result = list(map(lambda x : x+10,num))
# print(result)

# nums = [3,4,5,20,5]
# result = list(filter(lambda x: x%2 == 0 ,nums))
# print(result)


# num = [1,3,4,5,7]
# num.append(8)
# num.insert(2,100)
# num.remove(100)
# print(num)

# squares = [x*x for x in range(1,11)]
# print(squares)
# nums = [x for x in range(1,21)]
# even = [x for x in nums if(x%2 == 0)]
# print(even)

# nums =[x for x in range(1,11)]
# print(nums[::-1])

#TUPLE

# t = (2,3,34,45,[1,2,34,5])
# t[4].append(100)
# print(t)

# students = {
#     "name" : "Krishan",
#     "age": 18,
# }
# students["city"] = "Vrindavan"
# print(students["name"])
# print(students.get("ae")) #None will be the output.
# print(students.values())
# for values in students.values():
#     print(values)

# for key,value in students.items():
#     print(key,value)

# squares = {x: x*x for x in range(1,11)}
# print(squares)

# student1 ={
#     "name4": "Radha",
#     "age441": 17,
# }
# student2 ={
#     "name2":"Gopal",
#     "age2": 16,
# }
# students_dic = {**student1,**student2}
# print(max(students_dic))
# s = {1,2,3,4,5}
# s.add(6)
# s.remove(3)
# print(s)

# f = open("data.txt","w")
# f.write("Radhe Radhe sabhi ko.")
# f.close()


# f = open("data.txt","a+")
# f.write("\n Hare Krishna")
# f.close()

# f = open("data.txt","r")
# content = f.read()
# print(content)
# f.close()

# with open("data.txt", "r") as f:
#     print(f.readline())

#JSON
# import json
# python_dic = {
#     "name": "Krishna",
#     "age": 18,
#     "city": "Vrindavan"
# }
#python se json mtalab dump krna

# json_string = json.dumps(python_dic)
# print(json_string)

# import json
# json_data = {"name": "Radhe", "age": 16}

# # json se python banane ke liye
# pytho_dic = json.loads(json_data)
# print(pytho_dic)

# import json
# data = {
#     "name": "Gopal",
#     "age": 17,
#     "city": "Mathura"
# }

# with open("data.json","w") as f:
#     json.dump(data,f,indent=4)

# with open("data.json","r") as f:
#     content = json.load(f)
#     print(content)




#OOPs
# class student:
#     x = 5 #class variable
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#     def display(self):  #self se pata chalega ki kaunsa data use krna hai kaun object ne call kiya hai
#         print("Jai Jai Radharaman Pyaro Radharaman.")
        

# st = student("Krishna",14)
# st.y = 6 #adding new attribute to object
# st.display()
# # del st
# print(st.name,st.x)

# The pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

# class emptyclass:
#     pass

# name="Krishna"
# print("My name is",name)

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"Name: {self.name}, Age: {self.age}"

# p1 = Person("Radhe",16)
# print(p1)

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.graduationYear = 13

#     def display(self):
#         print(f"PARENT ::: Name is : {self.name},  Age is : {self.age}")

# class Student(Person):
#     def __init__(self,name,age):
#         Person.__init__(self,name,age)

#     def display(self):
#         print(f" CHILD ::: Name is : {self.name},  Age is : {self.age}, Grauation Year : {self.graduationYear}")

# p1 = Person("Krishna",14)
# p1.display()

# s1 = Student("Radhe",13)
# s1.display()

# class Vehicle:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def move():
#         print("MOVE!")

# class Car(Vehicle):
#     def __init__(self,brand,model):
#         pass
#     def move(self):
#         print("MOVE!")

# class Boat(Vehicle):
#     def move(self):
#         print("SAIL!")

# class Plane(Vehicle):
#     def move(self):
#         print("FLY!")
        
# C1 = Car("Ford","Mustang")
# B1 = Boat("Ibiza","Touring 20")
# P1 = Plane("Boeing","473")

# C1.move()
# B1.move()
# P1.move()

#OVERRIDING VS POLYMORPHISM

# Polymorphism allows us to define methods in the child class with the same name as defined in their parent class.
# This process of re-implementing a method in the child class is known as Method Overriding.
# class Animal:
#     def sound(self):
#         print("Animal makes a sound")     
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")


# def make_sound(animal):
#     animal.sound()
# dog = Dog()
# cat = Cat()
# make_sound(dog)
# make_sound(cat)


##ENCAPSULATION
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age

#     def display(self):
#         print(f"Name: {self.name}, Age: {self.__age}")

# p = Person("Radhe",13)
# p.display()

# p.__age 

# class Outer:
#     def __init__(self):
#         self.name = "Krishna"
#     class Inner:
#         def __init__(self,name):
#             self.name = name
#         def display(self):
#             print(f"{self.name}")
#     def display(self):
#             print(f"{self.name}")
# O = Outer()
# O.display()
# I = Outer.Inner("Radhe")
# I.display()


#NUMPY
# import numpy as np
# arr = np.array([1,2,3,4,5])
# print(arr)
# print(type(arr))


# import numpy as np
# arr = np.array(23)
# arr1 = np.array([1,2,3,4,5])
# arr2 = np.array([[1,2,3,4],[6,7,5,3]])
# arr3 = np.array([[[1,2,3,4],[6,7,5,3]],[[4,2,3,4],[6,7,8,3]]])
# arr4 = np.array([1,2,3,4,5], ndmin= 5)
# print(arr4.ndim)

# print(arr3[1,0,2])
# print(arr1[-3:-1])
# print(arr2[1,:3])
# print(arr2[1,2:])
# print(arr3[0,1,1:3])


# import numpy as np
# # arr = np.array(['a',2,3,4,5],dtype='i')
# # print(arr)
# # print(arr.dtype)

# # arr1 = np.array([2,3,34,5], ndmin=5)
# # print(arr1.shape)

# print(arr.shape)
# arr = numpy.array([1,2,4,5,5,6,6,5])
# newarr = arr.reshape(2,2,2)
# print(arr.reshape(2,2,2).base)


# import numpy as np
# arr = np.array([[[1,2,3,4,5],[6,7,8,9,12],[3,4,5,7,8]],[[13,14,15,16,17],[18,19,20,21,22],[3,5,6,3,5]]])
# for x in arr:
#     for y in x:
#         for z in y:
#             print(z)

# for x in np.nditer(arr):
#     print(x)


# arr = np.array([[1,4,3],[5,6,9]])
# arr1 = np.array([1,2,4,6,4,8])

# print(np.sum(arr , axis=0))  #column wise sum
# print(np.sum(arr , axis=1))  #

# print(np.mean(arr,axis=0))
# print(np.std(arr))

# arr = np.zeros((2,4))
# # arr = np.array([1,2,3,4,45])
# # arr = np.arange(4,10,2)
# print(arr)


# import numpy as np
# # arr = np.linspace(0,1,10)
# a = np.arange(10)
# b = np.arange(10,20)
# result = np.dot(a,b)

# c = np.arange(4).reshape((2,-1))
# d = np.arange(11,15).reshape(2,-1)
# result = np.dot(c,d)
# print(c)
# print(d)
# print(result)

# e = np.array(3)
# f = np.array(23)
# result = np.dot(e,f)
# print(result)

# import numpy as np

# a = np.arange(6).reshape(2, 3)
# b = np.arange(12).reshape(3, 4)

# print(np.dot(a, b))



#PANDAS
# import pandas as pd
# s = pd.Series([10,20,30,40],['a','b','c','d'])
# marks = {
#     "Math" : 85,
#     "Physics" : 78,
#     "Chemistry" : 100
# }
# s = pd.Series(marks)
# # print(s)

# data = {
#     "Name": ["Krishna","Radha","Gopal"],
#     "Age" : [21,22,24],
#     "Marks": [55,78,56]
# }
# data1 = {
#    " calories" : [12,3,344],
#    "duration" : [1,4,5]
# }
# df1 = pd.DataFrame(data1,['day1','day2','day3'])
# print(df1)
# df = pd.DataFrame(data)
# print(df)
# print(df["Name"])
# type(df["Name"])
# type(df[["Name"]])
# print("\n")
# print(df[["Name"]])
# print(df.loc[0,"Name"])
# print(df.iloc[2,2])
# print(df.shape)
# # print(df.info)
# print(df.head)

# import pandas as pd
# s = pd.Series([1,2,3],['a','b','c'])
# print(s)

# data = {
#     "calories": [324,3455,35],
#     "duration" : [34,43,34]
# }
# df = pd.DataFrame(data)
# print(df)

# df = pd.read_csv("students.csv")
# #csv mtalb comma seperated values
# print(df.head())
# print(df.shape)
# print(df.to_string())

# df = pd.read_csv("students.csv")
# print(df)
# print()
# print(df.loc[0,"Name"])
# print(df.iloc[0:3,0:3])
# print(df["Marks"] > 80)
# print(df[df["Marks"]>80])
# print(df[(df["Marks"]>80) & (df["Age"] < 25)])
# print(df.query("Marks > 80 and Age < 25"))
# print(df.isnull().sum())
# print(df.dropna())
# print(df.dropna(how="all"))
# df.dropna(inplace = True)
# print(df.dropna(subset=["Marks"]))
# df.fillna(130, inplace= True)
# print(df.to_string())

# print(df)
# print()
# # newdf = df.dropna(axis=0,how='all',inplace = False)
# # newdf1 = df.dropna(subset=["Marks"])
# newdf2 = df.dropna(thresh=2)

# print(newdf2)

# df1 = df.fillna({"Age": 18, "Marks":0})
# df1 = df.sort_values("Marks", ascending=False)
# df2 = df.sort_values(["Age", "Marks"], ascending=[True,False])
# print(df1)
# print('\n')
# print(df2)

# result = df.groupby('Age')["Marks"].max()
# result = df.groupby('Age')["Marks"].agg(['mean', 'max','min']).reset_index()
# result = df.groupby(['Age', 'City'])["Marks"].mean()

# print(result)


import pandas as pd
df = pd.DataFrame({ 
    "Name": ["Krishna","Gopal", "Radhe","Shyama","Hari"],
    "Class": [10,10,10,9,9],
    "Gender": ['M','M','F','F','M']
    "Marks":  [80,90,85,60,70]
})
print(df)

# /////////////////
# ///////


#

#

