
# 17.4->2
# info = [['Tina', 'Turner', 1939, 'singer'], ['Matt', 'Damon', 1970, 'actor'], ['Kristen', 'Wiig',
#                                                                                1973, 'comedian'], ['Michael', 'Phelps', 1985, 'swimmer'], ['Barack', 'Obama', 1961, 'president']]
# last_names = []
# for x in info:
#     last_names.append(x[0])
# print(last_names)


# 17.4->3
L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas',
                                                                 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]
b_strings = []
for x in L:
    for y in x:
        if 'b' in y:
            b_strings.append(y)
print(b_strings)
