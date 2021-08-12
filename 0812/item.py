import random

def item():
    cnt = 0
    while True:
        r = random.randint(1,100)
        #print(r)
        cnt = cnt + 1
        if r == 77:
            break;

    print(str(cnt) + "번째 뽑힌 아이템")

for i in range(100):
    item()
    
