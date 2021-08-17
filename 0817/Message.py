import tkinter
import tkinter.messagebox

def click_btn():
    tkinter.messagebox.showinfo("정보", "버튼을 눌렀습니다.")
    
root = tkinter.Tk()
root.geometry("640x480")
button = tkinter.Button(text = "테스트", command = click_btn)
button.pack()
root.mainloop()
