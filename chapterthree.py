#Practice project

def collatz(number):
    if number % 2 == 0:
        num = number // 2
        print(num)
        return num
    if number % 2 != 0:
        num = 3 * number + 1
        print(num)
        return num
    

        

print("Enter the number")
number = int(input())

while True:
   number = collatz(number)
   if (number == 1):
       break



        



 #fortune = random.randint(1,100)
# print (fortune)


# #function local scope
# def spam():
