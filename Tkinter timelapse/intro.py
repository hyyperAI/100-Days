from tkinter import *

window=Tk()
window.title("this is introductiory section")
# window.minsize(400,400)
window.config(padx=100,pady=50)

# importing image
canvas=Canvas(width=200,height=224)
img=PhotoImage(file="pngwing.com.png")
canvas.create_image(100,112,image=img)
canvas.create_text(100,112,text="hello come on!",font=("Arial",12,"bold"))
canvas.pack()


window.mainloop()