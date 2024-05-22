Python practice (Chapter Two)


What are the two values of the Boolean data type? How do you write them? 
True and False 

    2.  What are the three Boolean operators?
          and,or,not

    3.  Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).
   
True and True = True                                         c)not True                                                                                                                                                                                                                     
          True and False = False                                              False
          False and True = False
          False and False = False                                    d)not False
                                                                                          True                                      
     
 b)    True or True = True 
        False or True = True
        True or False = True
       False or False = False
4. What do the following expressions evaluate to? 

 (5 > 4) and (3 == 5)    =  False
 not (5 > 4)  =  True
 (5 > 4) or (3 == 5)   =  True
 not ((5 > 4) or (3 == 5))   =  False
(True and True) and (True == False)   = False
(not False) or (not True)  = True



5.  What are the six comparison operators?
    
       ==
       !=
       <=
       >=
       >
       <

6.   What is the difference between the equal to operator and the assignment operator? 
     
     Equal to operator is used for comparison of two value while the assignment operator              is used to store value in a variable

7.  Explain what a condition is and where you would use one.
    
  Condition is used to to check if the state of an expression, and this always come down            to a boolean value,true or false
They are used in control flow statement like if, while, and loop

8. Identify the three blocks in this code:
 spam = 0 
if spam == 10: 
print('eggs') 
if spam > 5: 
print('bacon') 
else: print('ham')
 print('spam') 
print('spam')
if ,if ,else

9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

In the vs code

10.  What can you press if your program is stuck in an infinite loop?
     
  break


11.What is the difference between break and continue?

     break is a shortcut used for the while loop to get out execution early.
     Continue causes the program to jump back to the beginning of the loop to revaluate the condition until it can get past the if statement


12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?

range(10)
The execution is from 0 to 9

range(0,10)
The execution will start from 0 but ends at 9

range(0,10,1)
The first execution will start from 0 to 10 but 1 will be the step argument the number of iteration that will occur in the first two argument


13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop. 
 
chaptertwo.py

14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

chaptertwo.py
