import re
import secrets
import string

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

def func():
    nums ='nums'
    lowercase = 'lcase'
    uppercase = 'ucase'
    special_chars = 's_chars'
    
    constraints =   [
                        (nums, 2),
                        (lowercase, 6),
                        (uppercase, 75),            
                        (special_chars, 9)           
                    ]
        # Check constraints
    for pattern, constraint in constraints:
        print(pattern, constraint)
func()