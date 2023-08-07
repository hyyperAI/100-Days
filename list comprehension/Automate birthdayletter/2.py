with open("D:/usman python/file.text" ,mode="r") as data:
    data.read()

with open("../../../file.text",mode="r") as data:
    # 2 step back and check folder , 2 more step back and check folder
    # ----> two folder back in second folder <-----
    data.read()


with open("C:/Users/Nexgen/OneDrive/Desktop/file.text",mode="r") as data:
    data.read()

# with open("../../../file.text")