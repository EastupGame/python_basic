#진단 게임 만들기
import tkinter
root = tkinter.Tk()
canvas = tkinter.Canvas(width = 800, height = 600)
canvas.pack()
mina = tkinter.PhotoImage(file = "mina.png")
canvas.create_image(400, 300, image = mina)
button = tkinter.Button(text = "진단하기", font = ("System", 32))
button.place(x = 400, y = 480)
text = tkinter.Text(width = 40 , height = 5, font = ("System", 16))
text.place(x = 320, y = 30)
root.mainloop()
