import tkinter
root = tkinter.Tk()
#체크 처리 함수 정의
def Check():
    if cval.get() == True:
        print("체크되어 있습니다.")
    else:
        print("체크되어 있지 않습니다.")

#체크 여부 확인하기
cval = tkinter.BooleanVar()         #BooleanVar()명령을 사용해 체크여부 확인객체생성
cval.set(True)
#체크 버튼 배치
checkbutton = tkinter.Checkbutton(text = "체크 버튼", variable = cval, command = Check)
checkbutton.pack()

root.mainloop()
