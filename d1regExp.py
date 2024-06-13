
#  search(),--- search the element in str--(if else bolck used)---.group() -- print whole word
#  findall(),--- used to find all element
#  match(),---only use for start of string MAtch==true
#  split(), --- used for non-alphanumeric code convrt into ,
#  sub()--(substitute)----- used for update the value



# program 1========================    search
#\w - [A-Z a-z 0-9]
# \d - digit 0 -9
# \b - blank space , space arround , ""
# \W+ - non numeric follwed by path
# \A - startwith string first character
# \z - endwith string last character
#  r - raw string
# #\W - non alphanumreic


str = 'cat man sun mpo run mat mm9 sun'
# [man mpo mat mm9]
#    ========= in search method onli one match can be find
e = re.search(r'm\w\w',str)
f = re.search(r'\wun',str)
# print(e)
# print(f)
# //it only find the match
# print(e.group())
# print(f.group())

#e # None---- python ---- false value
if e:
    print(e.group())
else:
    print("match not found !")

if f:
    print(f.group())
else:
    print("match not found")


strB  = "man sun mop run mat fat cat sat"
q1 = re.search(r'\wop',strB)
q2 = re.search(r'\wat',strB)
if q1:
    print(q1.group())
else:
    print("match not found")

if q2:
    print(q2.group())
else:
    print("match not found")

# ==============2) findall()== in this all find element can print
# q2 = re.findall(r'm\w\w',strB)
# q3 = re.findall(r'\wat',strB)
# print(q2)
# print(q3)


# program 3
# match() ==== only true for start of string
strC = "sun mon tue wed thu fri sat"
q4 = re.match(r"s\w\w",strC)
if q4:
    print(q4.group())
else:
    print("match not found")

#\W - non alphanumreic

# program 4
strD = "This; is the 'core' python's book"
q5 = re.split(r"\W+",strD)
print(q5)


#program 5
strE = "I am learning javascript"
q6 = re.sub(r'javascript','python',strE)
print(q6)

























