import re
string=input("reg no: ")
if re.match("(^[1-9][0-9][A-Z][A-Z][A-Z][0-9][0-9][0-9][0-9]$)",string) and string=="":
    print("matched!")
else:
    print("not matched!")
string2=input("email validation: ")
if re.match("(^[a-z0-9]*\@[a-z]+\.com$)",string2):
    print("email validated!!!\nGOOD ONE!")
else:
    print("wrong email syntax")
