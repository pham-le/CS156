letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
symbols = {}

for l in letters:
    ls = []
    for n in range(1,10):
        ls.append(l + str(n))
    symbols[l] = ls



#unary
for n in letters:
    for x in symbols[n]:
        print x + " gt 0"
        print x + " lt 10"

# quadrant
for x in letters: #letters
    for num in range(1,10):
        sym = x + str(num) #A1
        for y in range(1,10):
            if x+str(y) != sym:
                print sym + ' ne ' + x+str(y)
        sym = ''

# row 1
ls = []
for l in range(0, 3):
    for num in range(1,4):
        sym = letters[l]+str(num)
        ls.append(sym)
for x in ls:
    curr = x
    for y in ls:
        if y != curr:
            print curr + " ne " + y
#row 2
ls = []
for l in range(0, 3):
    for num in range(4,7):
        sym = letters[l]+str(num)
        ls.append(sym)
for x in ls:
    curr = x
    for y in ls:
        if y != curr:
            print curr + " ne " + y
#row 3
ls = []
for l in range(0, 3):
    for num in range(7,10):
        sym = letters[l]+str(num)
        ls.append(sym)
for x in ls:
    curr = x
    for y in ls:
        if y != curr:
            print curr + " ne " + y

#row 4
ls = []
for l in range(3, 6):
    for num in range(1,4):
        sym = letters[l]+str(num)
        ls.append(sym)
for x in ls:
    curr = x
    for y in ls:
        if y != curr:
            print curr + " ne " + y
#row 5
ls = []
for l in range(3, 6):
    for num in range(4,7):
        sym = letters[l]+str(num)
        ls.append(sym)
for x in ls:
    curr = x
    for y in ls:
        if y != curr:
            print curr + " ne " + y
#row 6
ls = []
for l in range(3, 6):
    for num in range(7,10):
        sym = letters[l]+str(num)
        ls.append(sym)
for x in ls:
    curr = x
    for y in ls:
        if y != curr:
            print curr + " ne " + y

#row 7
ls = []
for l in range(6, 9):
    for num in range(1,4):
        sym = letters[l]+str(num)
        ls.append(sym)
for x in ls:
    curr = x
    for y in ls:
        if y != curr:
            print curr + " ne " + y
#row 8
ls = []
for l in range(6, 9):
    for num in range(4,7):
        sym = letters[l]+str(num)
        ls.append(sym)
for x in ls:
    curr = x
    for y in ls:
        if y != curr:
            print curr + " ne " + y
#row 9
ls = []
for l in range(6, 9):
    for num in range(7,10):
        sym = letters[l]+str(num)
        ls.append(sym)
for x in ls:
    curr = x
    for y in ls:
        if y != curr:
            print curr + " ne " + y
#
#
# ###############
#
#
#column 4
ls = []
for l in [1,4,7]:
    for num in [1,4,7]:
        sym = letters[l]+str(num)
        ls.append(sym)
for x in ls:
    curr = x
    for y in ls:
        if y != curr:
            print curr + " ne " + y
#column 5
ls = []
for l in [1,4,7]:
    for num in [2,5,8]:
        sym = letters[l]+str(num)
        ls.append(sym)
for x in ls:
    curr = x
    for y in ls:
        if y != curr:
            print curr + " ne " + y
#column 6
ls = []
for l in [1,4,7]:
    for num in [3,6,9]:
        sym = letters[l]+str(num)
        ls.append(sym)
for x in ls:
    curr = x
    for y in ls:
        if y != curr:
            print curr + " ne " + y

#column 1
ls = []
for l in [0,3,6]:
    for num in [1,4,7]:
        sym = letters[l]+str(num)
        ls.append(sym)
for x in ls:
    curr = x
    for y in ls:
        if y != curr:
            print curr + " ne " + y
#column 2
ls = []
for l in [0,3,6]:
    for num in [2,5,8]:
        sym = letters[l]+str(num)
        ls.append(sym)
for x in ls:
    curr = x
    for y in ls:
        if y != curr:
            print curr + " ne " + y
#column 3
ls = []
for l in [0,3,6]:
    for num in [3,6,9]:
        sym = letters[l]+str(num)
        ls.append(sym)
for x in ls:
    curr = x
    for y in ls:
        if y != curr:
            print curr + " ne " + y

#column 7
ls = []
for l in [2,5,8]:
    for num in [1,4,7]:
        sym = letters[l]+str(num)
        ls.append(sym)
for x in ls:
    curr = x
    for y in ls:
        if y != curr:
            print curr + " ne " + y
#column 8
ls = []
for l in [2,5,8]:
    for num in [2,5,8]:
        sym = letters[l]+str(num)
        ls.append(sym)
for x in ls:
    curr = x
    for y in ls:
        if y != curr:
            print curr + " ne " + y
#column 9
ls = []
for l in [2,5,8]:
    for num in [3,6,9]:
        sym = letters[l]+str(num)
        ls.append(sym)
for x in ls:
    curr = x
    for y in ls:
        if y != curr:
            print curr + " ne " + y