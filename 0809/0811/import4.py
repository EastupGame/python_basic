import random
pl_pos = 1
com_pos = 1
def board():
    print("●" * (pl_pos - 1) + "P" + "●" * (30 - pl_pos))
    print("●" * (com_pos - 1) + "C" + "●" * (30 - com_pos))
    
while True:
    board()
    input("Enter키를 누르면 주사위 숫자가 나옵니다.")
    pl_pos = pl_pos + random.randint(1,6)
    com_pos = com_pos + random.randint(1,6)
