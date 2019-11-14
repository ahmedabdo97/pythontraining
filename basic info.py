import simplejson as json
import os

"""if: elif: else:"""
"""while: if: increment:"""
"""for in : result"""




"""def math_exp(num1,num2):
    return num1+num2

math1 = math_exp(5,75)
math2 = math_exp(8,72)
print("First sum is",math1,"2nd sum is",math2)"""




""" following argument for unlimited inserts * as list
def print_people(*people):
    for person in people:
        print("This person is",person)

print_people("Ahmed","Yasmeen","Abdullah","Asmahan")"""



"""def print_ahead(name = "Someone",age = "Unknown"):
    print("My name is",name,"& My age is",age)

print_ahead()"""

# newfile = open("newfile.txt", "w+")
# string = "this is the freakin content"
# newfile.write(string)

if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size !=0:
    old_file = open("./ages.json","r+")
    data = json.loads(old_file.read())
    print("Current Age IS", data["age"], "... adding a year")
    data["age"] = data["age"] + 1
    print("New age is", data["age"])
else:
    old_file = open("./ages.json", "w+")
    data = {'name' : 'Ahmed', 'age' : 27}
    print("No File Fount Setting Default age to ", data["age"])

old_file.seek(0)
old_file.write(json.dumps(data))