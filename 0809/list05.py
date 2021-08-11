QUESTION = ["한세사이버보안고가 있는 구는?",
            "한세사이버보안고에서 가장 가까운 지하철 역은",
            "한세사이버보안고의 교화는?"]
R_ANS = ["마포구","애오개역","매화"]

for i in range(3):
    print(QUESTION[i])
    ans = input()
    if ans == R_ANS[i]:
        print("정답입니다.")
    else:
        print("오답입니다.")


