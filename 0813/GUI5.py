import tkinter

root = tkinter.Tk()

canvas = tkinter.Canvas(width = 400, height = 600, bg = "skyblue")
canvas.pack()
player = tkinter.PhotoImage(file = "player.png")
canvas.create_image(200,300, image = player )

root.mainloop()
