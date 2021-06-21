#writing a code  to find out whether given input values form a square or not
def finding_the_shape(length,breadth):
    if (length==breadth):
        print("Yes")
    else:
        print("No")
    return length
        


length=input("")#taking variable for use inputs
breadth=input("")
finding_the_shape(length,breadth)#calling the function