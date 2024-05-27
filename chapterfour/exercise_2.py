# Write a function that takes a list value as an argument and returns
# a string with all the items separated by a comma and a space, with and
# inserted before the last item. For example, passing the previous spam list to
# the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it.
# #Practice project

#Todo: Create a function that takes in a list as an argument and returns a string
#Todo: Loop through the items 
#Todo: For each item in the list, add to a string and it should be separated by a comma and a space
#Todo: If I am at the last item insert and

def spam(list_items):
    finalist_list = ""
    if len(list_items) == 1:
        return  list_items[0]
    for index in range(0,len(list_items)): 
        
        if index == len(list_items) - 1 :
            finalist_list += "and " + list_items[index]
        else:
            finalist_list += list_items[index]+ "," + " "
    return finalist_list

print(spam(["banana"]))

