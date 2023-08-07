import pandas

with open("../../Day 24 , File_handling/Default_letter_outllok/send_application.docx", encoding="latin-1") as letters:
    """read the file and encoding help to read file"""
    start_final = (letters.read())

data = pandas.read_csv("./reg.csv")
"""this read csv file and save it's data in data variable"""
names = data.Name.to_list()

# these codes have specific information related to the others
registration = data.Reg_No.to_list()
day = data.Day.to_list()
date = data.Date.to_list()

for item in range(0, 3):
    print(f"{names[item]},{registration[item]},{day[item]},{date[item]}")

    with open(f"./final_letters./ready to send to {names[item]}.docx", mode="w", encoding="latin-1") as final_letters:

        final_letters.write(
            start_final.replace("name", str({names[item]})).replace("date", str({date[item]})).replace("day", str({day[
                                                                                                                       item]})).replace(
                "reg", str({registration[item]})))

