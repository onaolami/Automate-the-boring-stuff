# Table Printer
# Write a function named printTable() that takes a list of lists of strings
# and displays it in a well-organized table with each column right-justified.
# Assume that all the inner lists will contain the same number of strings.
# For example, the value could look like this:
# tableData = [['apples', 'oranges', 'cherries', 'banana'],
# ['Alice', 'Bob', 'Carol', 'David'],
# ['dogs', 'cats', 'moose', 'goose']]
# printTable() function would print the following:
# apples Alice dogs
# oranges Bob cats
# cherries Carol moose
# banana David goose

#Thought Process
#Write a function named printTable()


def printTable(tableData):
    for col in range(0, len(tableData[0])):
        items = ""
        for row in range(0, len(tableData)):
            items += tableData[row][col] +" "
        print(items)

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice',  'Bob',     'Carol',    'David'],
             ['dogs',   'cats',    'moose',    'goose']]

printTable(tableData)