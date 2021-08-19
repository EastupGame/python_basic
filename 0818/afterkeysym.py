import tkinter
key = ""
def key_down(e):
    global key
    key = e.keysym

def main_proc():
    label["text"] = key
    root.after(100, main_proc)
    
root = tkinter.Tk()
root.title("실시간 키 입력 처리")
label = tkinter.Label(font = ("System", 80))
label.pack()
root.bind("<KeyPress>", key_down)
main_proc()
root.mainloop()
