import tkinter
tmr = 0         #전역변수
def count_up():
    global tmr     #tmr을 전역변수로 취급하기 위한 선언
    tmr = tmr + 1
    label["text"] = tmr
    root.after(1000, count_up)
    
root = tkinter.Tk()
label = tkinter.Label(font = ("System", 80))
label.pack()
root.after(1000, count_up) 
root.mainloop()
