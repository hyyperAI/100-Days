import pandas as pd
import random
number=[1,2,3]
new_list=[item+2 for item in number]
print(new_list)
names=["Sajid","Usman","Rehan","Fazeel","AliJan","Ahmad-Hassan"]

new_names=[item.upper() for item in names if len(item)==5]

first_list=[]
second_list=[]
with open("./text1.txt",mode="r") as new_file:
    data1=new_file.readlines()
    for item in data1:
        first_list.append(int(item.strip()))
print(first_list)

with open("./text2.txt",mode="r") as new_file:
    data2=new_file.readlines()
    for item in data1:
        second_list.append(int(item.strip()))
# #  <-------- OR --------->

with open("./text1.txt",mode="r") as new_file:
    data1=new_file.readlines()
#
with open("./text2.txt",mode="r") as new_file:
    data2=new_file.readlines()

result=[int(item) for item in data1 if item in data2]
print(result)
#         # ------------ DICTIONARY
#
new_dict={x:random.randint(1,100) for x in names }
print(new_dict)

sentence="What is the Airspeed Velocity of an Unladen Swallow?"
new_dict2={word:len(word) for word in sentence.split() }
print(new_dict2)

weather_c={
    "Mpnday":12,
    "Tuesday":14,
    "Wednesday":15,
    "Thursday":14,
    "Friday":21,
    "Saturday":22,
    "Sunday":24,
}
weather={
    "Days":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
    "Temperature_in_C":[12,14,15,14,21,22,24]
}
#
#
# #  importing through the panda library dictionary / looping through panda Dataframe
#
weather_dataframe=pd.DataFrame(weather)
print(weather_dataframe)
#iterrow provide to compare two rows or columns in it.
for (key,value) in weather_dataframe.iterrows():
    print(key ,value)
    print(key)
#
#
print(weather_dataframe.iterrows())
x=[(row.Temperature_in_C) for (index,row) in weather_dataframe.iterrows() if index==1] # of particular row or data
print(x)

y={row.Days:(row.Temperature_in_C) for (index,row) in weather_dataframe.iterrows() if index==1}
print(y)
# of particular row or data




