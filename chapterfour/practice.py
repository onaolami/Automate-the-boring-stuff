# Create a function that returns the number of odd numbers in a list e.g 

# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Todo: Create a function that has the number list as the argument
#Todo: Loop through the number list
#Todo: If num  % 2 == 1 its an odd number else its even


def spam(number_list):
    num = 0
    for item in number_list:
        if item % 2 == 1:
            num += 1
    return num

print(spam([1,2,3,4,5,6,7,8,9,10]))

