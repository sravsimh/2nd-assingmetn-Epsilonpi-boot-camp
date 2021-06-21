#defining function to reverse the list formed by given words




string1=input("")#assinging variables

_list=[string1]#aading the input variables to lists
name=""#defining a empty string to use in for loop
for items in _list:
    name+=items
print(name[::-1])#reversing the string using print function#
