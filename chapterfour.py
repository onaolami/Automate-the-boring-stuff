
    
myList = ['apples','bananas','tofu','cats']
for x in myList:
    print(x)

def spam (myList):
    num = len(myList)
    finalList = ""
    for x in range(num):
        if x < num - 2:
            finalList = finalList + myList[x] + ", "
        elif x < num - 1:
            finalList = finalList + myList[x] + ", and "
        else:
            finalList = finalList + myList[x] 
    return finalList


print(spam(myList))




# spam = [['cat', 'bat'], [10, 20, 30, 40, 50,60]]

# print(spam [1], [4])

# spam = ['cat', 'bat', 'rat', 'elephant']

# print(spam[-1])


# eggs = ["hello","chicken"]
# eggs.insert(1,"world")

# print(eggs)