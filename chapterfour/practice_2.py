# Create a function that returns the SUM of all the numbers in a list e.g 

# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Create a function that passes the argument of number_list
# Loop through the item
# Create a variable Sum
# Return the  sum of all the numbers in a list


def spam(number_list):
    sum = 0
    for item in number_list:
        sum += item
    return sum


print(spam([1,2,3,4,5,6,7,8,9,10]))
