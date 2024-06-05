1. What is the function that creates Regex objects?
   re.compile()

2. Why are raw strings often used when creating Regex objects?
   Raw strings are often used when creating Regex objects because they prevent the need for double escaping.
   
3. What does the search() method return?
   This method in regular expressions returns a match object if the pattern is found within the string

4. How do you get the actual strings that match the pattern from a Match
  object?
   To get the actual strings that match the pattern from a Match object, you can use the group() 

5. In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)' , what does
   group 0 cover? Group 1 ? Group 2 ?
   
    Group 0 covers the entire matched string.
    Group 1 covers the first three digits of the first number.
    Group 2 covers the entire second number along with the hyphen.

6. Parentheses and periods have specific meanings in regular expression syntax. How would you specify that you want a regex to match actual parentheses and period characters?
  
  Match them using a "\" to escape the characters

7. The findall() method returns a list of strings or a list of tuples of
   strings. What makes it return one or the other?

    
8. What does the | character signify in regular expressions?
    This represents OR


9.What two things does the ? character signify in regular expressions?

The ? character can signify both optionality and non-greediness in regular expressions.



10. What is the difference between the + and * characters in regular
   expressions?

   The * matches zero or more of the preceding group.
    The + matches one or more of the preceding group.



11. What is the difference between {3} and {3,5} in regular expressions?
  {3}Matches the preceding element exactly three times.
  {3,5} Matches the preceding element between 3 to 5


12. What do the \d , \w , and \s shorthand character classes signify in regular
expressions?

  \d , \w , and \s match a digit, word, or space character, respectively.


13. What do the \D , \W , and \S shorthand character classes signify in regular
expressions?
   \D , \W , and \S match anything except a digit, word, or space character,

14. How do you make a regular expression case-insensitive?
    By passing re.IGNORECASE or re.I as a second argument to re.compile() .

15. What does the . character normally match? What does it match if
re.DOTALL is passed as the second argument to re.compile() ?


16. What is the difference between .* and .*? ?
.* is greedy, matching as many characters as possible, while .*? is non-greedy, matching as few characters as possible.


17. What is the character class syntax to match all numbers and lowercase
letters?


18.If numRegex = re.compile(r'\d+') , what will numRegex.sub('X', '12 drummers,
11 pipers, five rings, 3 hens') return?


19.What does passing re.VERBOSE as the second argument to re.compile()
allow you to do?

20.How would you write a regex that matches a number with commas for
every three digits? It must match the following:
• '42'
• '1,234'
• '6,368,745'
but not the following:
• '12,34,567' (which has only two digits between the commas)
• '1234' (which lacks commas


    
     

