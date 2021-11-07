"""lis, running, temp = [], 1, 0
while True:
    x = input("Enter a number or quit: ")
    if x != "quit": lis.append(int(x))
    else: break

while running != 0:
    running = 0
    for x in range(len(lis)-1):
            if lis[x] > lis[x+1]:
            temp = lis[x]
            lis[x] = lis[x+1]
            lis[x+1] = temp
            running += 1
print(lis)"""
"""
lis, running, temp = [], 1, 0
while True:
    x = input("Enter a number or quit: ")
    if x != "quit": lis.append(int(x))
    else: break

while running != 0:
    running = 0
    for x in range(len(lis)):
        if x+1 != len(lis):
            if lis[x] < lis[x+1]:
                temp = lis[x]
                lis[x] = lis[x+1]
                lis[x+1] = temp
                running += 1
print(lis)"""
"""
from random
def gen(n):
    lis = []
    for x in range(n):
        lis.append(x)
    return lis


lis, running, temp, comparison_count, exchange_count, passes_count = [], 1, 0, 0, 0, 0
while True:
    x = input("Enter a number or quit: ")
    if x != "quit": lis.append(int(x))
    else: break

while running != 0:
    running = 0
    for x in range(len(lis)-1):
            if lis[x] > lis[x+1]:
                temp = lis[x]
                lis[x] = lis[x+1]
                lis[x+1] = temp
                running += 1
                exchange_count += 1
            comparison_count += 1
    passes_count += 1

print(lis,"\nNumber of comparisons",comparison_count,"\nNumber of exchanges",exchange_count,"\nNumber of passes", passes_count)
 
print(gen(int(input("Enter a number: "))))
"""
"""
r = int(input("Enter a number: "))

y = int(input("Enter a number: "))
q = 0

while r >= y:
    r -= y
    q += 1
print(r, q)
"""
"""
n = int(input("Enter a number: "))
while n < 1: n = int(input("Enter a number: "))
for i in range(n):
    i += 2
    while n%i == 0:
        print(i)
        n = n / i
"""
"""
import math
n = int(input("Enter a number: "))
while n <= 1: n = int(input("Enter a number: "))
sqrtofn = math.floor(math.sqrt(n))
for i in range(sqrtofn):
    i += 2
    while n%i == 0:
        print(i)
        n = n / i
if n > 1: print(n)
"""
