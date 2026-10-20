import math 
PI=3
print ("give the number of digits")
digit_number=int(input())
n=2
while n<digit_number:
    if ((n/2)% 1 != 0)==True:
        #print ("true")
        new_number = PI - (4/((2+(n-2)*2)*(2+(n-2)*2+1)*(2+(n-2)*2+2)))
    else:
        #print ("false")
        new_number = PI + (4/((2+(n-2)*2)*(2+(n-2)*2+1)*(2+(n-2)*2+2)))
    PI=new_number
    #print (PI)
    print (PI)
    n=n+1
print ("result")
print (PI)