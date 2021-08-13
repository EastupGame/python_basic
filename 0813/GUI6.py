import random
import tkinter


def click_btn():
    label["text"] = random.choice(["1","2","3","4","5"])
    label.update()

root = tkinter.Tk()
root.resizable(False, False)
canvas = tkinter.Canvas(width = 800, height = 600, bg = "skyblue")
canvas.pack()
player = tkinter.PhotoImage(file = "player.png")
canvas.create_image(200,300, image = player )

label = tkinter.Label(root, text = "??", font = ("System", 120))
label.place(x = 380, y = 60)

button = tkinter.Button(root, text = "숫자카드를 뽑아주세요.",
                        font = ("System", 40), command = click_btn )
button.place(x = 380, y = 480)
root.mainloop()
