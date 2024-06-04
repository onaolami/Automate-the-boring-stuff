# Create a function that takes in 2 list arguments of same length.
# If the lengths of the list are not the same your program should return an empty list. 
# If the length of the lists are equal your program should combine both lists together and return a single list. e.g
# list_1 = ["bayo", "dayo", "shayo", "rayo"]
# list_2 = ["moyo", "tayo", "fayo", "gbayo"]

# the result of this example should be:

#  ["bayo", "moyo", "dayo", "tayo, "shayo", "fayo", "rayo", "gbayo"]


# Create a function that takes 2 list argument

# If length of the  list are not the same return empty list


# Create a loop 

#return the joint list

def spam(list_1, list_2):
     if len(list_1) != len(list_2):
        return []
     
     joint_list = []
     for index in range(len(list_1)):
        joint_list.append(list_1[index])
        joint_list.append(list_2[index])
        
     return joint_list


list_1 = ["bayo", "dayo", "shayo", "rayo"]
list_2 = ["moyo", "tayo","fayo"]

result = spam(list_1,list_2)

print(result)