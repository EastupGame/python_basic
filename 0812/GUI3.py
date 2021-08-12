import tkinter
root = tkinter.Tk()
root.title("첫번째 레이블")
root.geometry("800x600")
label = tkinter.Label(root, text = "사라진 알파벳을 찾아라!", font = ("System",48) )
label.place(x = 80, y = 50)
root.mainloop()
