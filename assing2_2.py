#defining a function to covert the input into strings and out to strings
def string_converter(name,age):
    age=str(age)
    print(f"{name} {age}")
    return name


name=input("")#defining variables
age=str(input(""))
string_converter(name,age)#function call
