lis = []
lis2 = []
for _ in range(5): 
    lis.append(input("fil: "))
    lis2.append(input("dir: "))
print(lis)

x = input(": ") 
if x in lis: print("Ok", lis.index(x))
else: print("Not Found")

film_num = int(input("fil num: "))
print(lis[film_num-1],lis2[film_num-1])