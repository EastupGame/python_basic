import tkinter

def click_btn():
    text.insert(tkinter.END, "몬스터가 나타났다!")
    
root = tkinter.Tk()

button = tkinter.Button(text = "버튼", command = click_btn)
button.pack()

text = tkinter.Text()
text.pack()

root.mainloop()
