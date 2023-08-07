import pandas

data=(pandas.read_csv("data_of_students.csv"))
pandas.set_option("display.max.columns", None)
# totals=data.groupby("Student Name").sum().sort_values()
# print(totals)
person=(data[data["Student Name"]=="Anzish"])
peshawar_count=(data[data["Domicile Name"]=="Peshawar"])
print(peshawar_count)
these={
    peshawar_count["Student Name"]:[peshawar_count["Domicile Name"]],
    peshawar_count["Student Name"]:[peshawar_count["Father Name"]]
}
# print(dict)
# peshawar=pandas.DataFrame(peshawar_count)
# peshawar.to_excel("Peshawar Students")
#nrows

# print(person)