Chapter 5

 1. What does the code for an empty dictionary look like?
           { }

2.What does a dictionary value with a key 'foo' and a value 42 look like?

       {“foo””:42”}

3. . What is the main difference between a dictionary and a list?

  Dictionary contains key and value, each value is separated by semicolon and curly braces are you used here,while a list is an ordered collection of items they are stored in square bracket


4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
     This will raise an error because the key foo is not in the dictionary of spam


5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?

  ‘Cat’ in spam is used to check if the key cat is present in the dictionary spam  while  Cat’ in spam.keys() this when we are trying retrieve the key in spam, it also checks if they cat is present in the dictionary of spam.



6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?

     
‘Cat’ in spam is used to check if the key cat is present in the dictionary spam while ‘cat’ in spam values is used check if there's any values assigned to the key spam 



7. What is a shortcut for the following code? if 'color' not in spam: spam['color'] = 'black'

 spam.setdefault(‘color’:’black’)



8.What module and function can be used to “pretty print” dictionary values?

pprint () function which the module can be imported


