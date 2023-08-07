import pandas

park_data=pandas.read_csv("4.3 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(park_data.columns)
# print(park_data["Age"])
grey_count=(len(park_data[park_data["Primary Fur Color"]=="Gray"]))
# acess the park_data then in park_Data access Primary Fur Color then check out the one with unique color
red_count=(len(park_data[park_data["Primary Fur Color"]=="Cinnamon"]))
black_count=(len(park_data[park_data["Primary Fur Color"]=="Black"]))

print(grey_count)
print(red_count)
print(black_count)

dict_park_data={
    "Fur_color":['Gray','Cinnamon',"Black"],
    "Count":[grey_count,red_count,black_count]
}
csv_park_data=pandas.DataFrame(dict_park_data)
# print(csv_park_data)
csv_park_data.to_csv("park_Primary_Fur_Color")

