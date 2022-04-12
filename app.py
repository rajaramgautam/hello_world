print('Rajaram')
print("*" * 11)

print('hello')

x = 1
# Variables

student_count = 1000
print(student_count)
is_published = True

print(is_published)

# Variable_Names
# Make sure your variable name are descriptive
# Lower case name for variable name
# Use underscore to separate words in varaible names

# Strings 

course = "Python Programming"


message =  """Hello Julian,

I am Rajaram Gautam. We need to make another offer.

Can you talk on it please?


"""

print(message)

print(len(message))
print(message[0])

# Escape Character \
    
course_name = "Python \"Programming" # Backlash ignoring the character after it

print(course_name)

# Hash sign for commenting single line
# \n  to add new line


# String Methods
print(course_name)

# numbers
"""
/ regular division
// gives us quotient only
% will give us a remainder only
** works like power

"""

age = int(input('Please tell me your age: '))

age_after_10_year = age + 10
 
print(age_after_10_year)

# Falsy Values

# "" empty string
# 0
# None 

# Comparision Operators

# Conditional Statements

temperature = 20

if temperature > 30:
    print("Its warm.")
    print("Drink water.")
elif temperature > 25:
    print("Its nice.")
    
else:
    print("Its cold.")
print("Done")

# Ternary Operator

# Logical Operator
# and, or, not

high_income = True
good_credit = True

if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")