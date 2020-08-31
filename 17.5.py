nested1 = [1, 2, ['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h']]
for x in nested1:
    print("level1: ")
    if type(x) is list:
        for y in x:
            print(f"     level2: {y}")
    else:
        print(x)
