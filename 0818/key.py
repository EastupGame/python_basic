import tkinter
key = 0
def key_down(e):
    global key
    key = e.keycode
    print("KEY:" + str(key))
    
root = tkinter.Tk()
root.title("키 코드 얻는 프로그램")
root.bind("<KeyPress>", key_down )
root.mainloop()
