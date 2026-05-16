#TypeCasting = is the process of converting a variable from one datatype to another
#               str(), int(), float(), bool()

name = "Anush Pote"
age = 22
gpa = 2.99
is_student = True

print(f"The datatype of name:{type(name)}")
print(f"The datatype of age:{type(age)}")
print(f"The datatype of gpa:{type(gpa)}")
print(f"The datatype of is_student{type(is_student)}")

# converting float(gpa) to integer

gpa = int(gpa)

print(f"After changing the type of gpa to integer: {gpa}")

# converting integer(age) to float

age = float(age)

print(f"After changing the data type of age to float: {age}")

# type integer(age) to string

age = str(age)

print(f"The datatype of age has been changed to string: {type(age)}") 

#age += 1
#print(age) output:#TypeError: can only concatenate str (not "int") to str

age += "1"

print(f"Adding 1 to age to see what happens: {age}")

#changing string(name) to bool
