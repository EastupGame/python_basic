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
bVar = [None] * 7
cbtn = [None] * 7
ITEM = [
    "높은 곳이 좋다.",
    "공을 보면 굴리고 싶어진다.",
    "깜짝 놀라면 털이 곤두선다.",
    "쥐구멍이 마음에 든다.",
    "개에게 적대감을 느낀다.",
    "생선 뼈를 발라 먹고 싶다.",
    "밤, 기운이 난다."
]
for i in range(7):
    bVar[i] = tkinter.BooleanVar()
    bVar[i].set(False)
    cbtn[i] = tkinter.Checkbutton(text = ITEM[i], font = ("System", 12),variable = bVar)
    cbtn[i].place(x = 400, y = 160 + 40 * i)

root.mainloop()
