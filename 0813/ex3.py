import tkinter
import random
def click_btn():
    label_result["text"] = random.choice(["1개", "2개","5개","10개","20개"])
    label_result.update()
    
root = tkinter.Tk()

canvas = tkinter.Canvas(width = 800, height = 700, bg = "lightgray")
canvas.pack()

label_title = tkinter.Label(text = "묵!찌!빠!", font = ("KCC무럭무럭", 80))
label_title.place(x = 200, y = 50)

gawebawebo = tkinter.PhotoImage(file = "gawebawebo.png")
canvas.create_image(400,300, image = gawebawebo )

label_result = tkinter.Label(text = "??", font = ("KCC무럭무럭", 80))
label_result.place(x = 350, y = 400)

button = tkinter.Button(text = "버튼", font = ("KCC무럭무럭", 30),
                        command = click_btn)
button.place( x = 355, y = 600)

root.mainloop()
