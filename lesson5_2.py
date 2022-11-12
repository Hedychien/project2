#一個專案內的主執行的py檔,必需要使用__name__的判斷式
'''
這是一個猜數字遊戲
'''

import random

if __name__ == "__main__":
    min = 1
    max = 50
    count = 0
    random_value = random.randint(min,max)
    print("====猜數字遊戲====")
    while True:
        count += 1
        keyin = int(input(f"猜數字的範圍{min}~{max}:"))
        if keyin >= min and keyin <= max :
            if(keyin == random_value):
                print(f"Hooray! 猜對了，答案是:{random_value}")
                print(f"您共猜了{count}次")
                break
            elif keyin > random_value:
                print("再小一點")
                max = keyin - 1
            elif keyin < random_value:
                print("再大一點")
                min = keyin +1
            print(f"您已猜了{count}次")
        else:
            print(f"{keyin}超出範圍")
    print("Game over!")