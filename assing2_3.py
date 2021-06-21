#defining a function to print the first 10 multiples of user input
def multipiles(number):
    i=1
    while i<=10:
        print(number*i)
        i+=1
    return number



number=int(input())#defining user input variable
multipiles(number)#function call
