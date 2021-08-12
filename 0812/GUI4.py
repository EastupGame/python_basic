import tkinter
def click_btn():
    button["text"] = "클릭했군요!"
    
root = tkinter.Tk()
root.title("첫번째 버튼")
root.geometry("800x600")
button = tkinter.Button(root, text = "버튼 문자열", font = ("System", 20),
                        command = click_btn )
button.place(x = 400, y = 300) 
root.mainloop()
