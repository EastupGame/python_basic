import tkinter

root = tkinter.Tk()
root.resizable(False, False)
canvas = tkinter.Canvas(width = 800, height = 600, bg = "skyblue")
canvas.pack()
player = tkinter.PhotoImage(file = "player.png")
canvas.create_image(200,300, image = player )

label = tkinter.Label(text = "??", font = ("System", 120))
label.place(x = 380, y = 60)

button = tkinter.Button(text = "슛 넣을 확률", font = ("System", 40))
button.place(x = 380, y = 480)
root.mainloop()
