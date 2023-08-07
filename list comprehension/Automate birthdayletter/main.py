with open("./input/names/names_final.txt") as names:
    name_list = names.readlines()

# this code read names file and convert it in list : readlines()

with open("./input/letters/starting_letter2.docx") as letters:
    start_final = (letters.read())

    # this code read letter over_all seen and then save it in start_final

    for item in name_list:
        name = item.strip()

        # striping extra details instead of name : "\n"

        with open(f"./output/readytosend/letter_for_{name}.docx", mode="w") as ready:
            ready.write(start_final.replace("Angele","usman"))

# writing names and creating letters.
