
import re
# program 6
# [A-Z , a-z , 0-9] // alphanumric  // " ", %%%
# [/W] --- " " and special symbol
# [/w]* zero or more repetitions
# \d  -- represents only digits
# \b -- only blank space


str6 = "an apple a day keeps doctor away"
e2 = re.findall(r'\ba[\w]*',str6)   # ["an", "apple" , a , ay,away]
print(e2)

# [\w]*---one or more character

# program 7
str7 = "The meeting will be conducted on 1stttr and 21st of each month"
e3 = re.findall(r'\d[\w]*',str7)
print(e3)


# program 8
str8 = "one two three four five six seven 8 9 10"
e4 = re.findall(r'\b\w\w\w\w\w',str8)
print(e4)

# \w{5} -- used for how many no. of character you want
str8 = "one two three four five six seven 8 9 10"
e4 = re.findall(r'\b\w{5}',str8)
print(e4)
str8 = "one two three four five six seven 8 9 10"
e4 = re.search(r'\b\w{5}',str8)
print(e4.group())

# program 9
str9 = "one two three four five six seven nineteen 8 9 10"
e5 = re.findall(r'\b\w{4,}',str9)
print(e5)
# {3,5}--- range
#program 10
str9 = "one two three four five six seven nineteen 8 9 10"
e5 = re.findall(r'\b\w{3,5}\b',str9)
print(e5)
# {1,}--- one or more
# program11
str6 = "one two three four five six seven nineteen 8 9 10"
e6 = re.findall(r'\b\d{1,}\b',str6)
e7 = re.findall(r'\b\d+\b',str6)
print(e6)
print(e7 )


#program12
# a regular expression to find last word starting with 's'
# a regular expression to find last word starting with 'o'
str6 = "o one two three four five six seven seventeen two"
# '\Z' 0 end of string
# '\A' start of string

e8 = re.findall(r'\bs[\w]*\Z',str6)
e9 = re.findall(r'\A\bo[\w]*',str6)
print(e8)
print(e9)












