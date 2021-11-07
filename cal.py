def add(x,y): return x + y
def sub(x, y): return x - y
userchoice, x, y = input("mode: "), int(input("num 1: ")), int(input("num 2: "))
if userchoice == "add": print(add(x,y))
elif userchoice == "sub": print(sub(x,y))