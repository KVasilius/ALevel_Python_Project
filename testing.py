x = [("a","b"),("a","c"),("a","d")]
z = "d"
for y in range(len(x)): 
    print
    if z in x[y][0] or z in x[y][1]: 
        print("yes")