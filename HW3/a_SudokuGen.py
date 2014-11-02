letters = ['nothing', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

for x in range(1, 10):
    for y in range(1, 10):
        #unary constraints
        print letters[x] + str(y), 'gt', 0
        print letters[x] + str(y), 'lt', 10
for x in range(1, 10):
    for y in range(1, 10):
        #row constraints
        for x2 in range(1, 10):
            if x != x2:
                print letters[x] + str(y), 'ne', letters[x2] + str(y)
        #column constraints
        for y2 in range(1, 10):
            if y != y2:
                print letters[x] + str(y), 'ne', letters[x] + str(y2)
        #block constraints
        def threes(num):
            num -= 1
            return 1 + (num - (num % 3))
        for x2 in range(threes(x), threes(x) + 3):
            for y2 in range(threes(y), threes(y) + 3):
                if not (x == x2 or y == y2):
                    print letters[x] + str(y), 'ne', letters[x2] + str(y2)
