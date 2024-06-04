#write a program that return true if a number exist in an array. 
#In your program create a function that takes two arguments,the array and the number you want to search for

#Todo

# Create a function that takes two argument, array and number.
# Loop through the array to check if number exist
# If exist it should true

def spam(array,number):
    for item in array:
        if number == item:
            return True
    return False


array = [1,2,3,4,5]
number = 1

result = spam(array,number)

print(result)