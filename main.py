#Samuel Wylie 12/9/2023
#Lists introduction script

def unduplicate(list):
    templist = []
    for i in list:
        if i in templist:
            pass
        else:
            templist.append(i)
    print(templist)


items = []

while True:
    newItem = input('Please add an item to the list. If you wish to add no more, type N ')
    if newItem == 'N':
        break
    else:
        items.append(newItem)
        print(items)

unduplicate(items)
