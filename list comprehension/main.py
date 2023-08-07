import pandas as pd
csv_file=pd.read_csv("./nato_phonetic_alphabet.csv")
df_csv=(pd.DataFrame(csv_file))
dict_of_csv={value.letter:value.code for(index,value) in df_csv.iterrows()}
print(dict_of_csv)
list_of_words=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","U","R","S","T","U","V","W","X","Y","Z"]


def generator():
    user_word=input("Enter Word: ").upper()
    out_put_list=[dict_of_csv[item] for item in user_word]
    print(out_put_list)

generator()