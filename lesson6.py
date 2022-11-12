def sayHello(): #沒有參數的function
    print("Hello!")

def sayHello_withName(name): #有參數的function
    print(name)

def square_area(side):    #有一個參數的function，同時有傳出值
    area = side **2       #此area為function變數
    return area


if __name__ == "__main__":
    sayHello()
    sayHello_withName("Hedy")    #引數值傳遞至name參數內
    side = eval(input("請輸入正方形的邊:"))
    area = square_area(side)    #此area為文件變數
    print(f"正方形,一邊為{side}, 面積為{area}")


