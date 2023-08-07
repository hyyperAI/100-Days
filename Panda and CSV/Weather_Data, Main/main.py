import pandas
data=pandas.read_csv("weather_data.csv")

temp_list=data["temp"].to_list()
#--->  AVERAGE <----

average=sum(temp_list)/len(temp_list)

#  ---->OR<----
average1=data["temp"].mean()

# MAXIMUM SERIES VALUE:
print(data["temp"].max())


print(data.condition)
# print row of data which has highest temperature

print(data[data.temp==data.temp.max()])

# accesing the particular data:

monday=data[data.day=="Monday"]
# now we access the variable holding a particular data
# for checking the condition
temp_in_C=(monday.temp)
temp_in_F=(temp_in_C*1.8)+32
print(temp_in_F)

data_dict={
    "Reg_No":[897,765,467],
    "Name":["Talha","abuzar","Rehan"],
    "Day":["Monday","Wednesday","Thursday"],
    "Date":["2/3/2033","5/4/2023","5/8/2023"]
}

admission=pandas.DataFrame(data_dict)

print(admission)
admission.to_csv("reg.csv")


