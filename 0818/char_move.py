import tkinter
key = ""
px = 400
py = 300
def key_down(e):
    global key
    key = e.keysym

def main_proc():
    global px, py
    if key == "Right":
        px = px + 10
    canvas.coords("PLAYER", px, py)    
    root.after(100, main_proc)

root = tkinter.Tk()
root.title("실시간 키 입력 처리")
canvas = tkinter.Canvas(width = 800, height = 600)
canvas.pack()
player = tkinter.PhotoImage(file = "player.png")
canvas.create_image(px,py,image = player, tag = "PLAYER")

root.bind("<KeyPress>", key_down)
main_proc()
root.mainloop()
