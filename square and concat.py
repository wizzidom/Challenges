#Myxzptlk
#This  gives out the square of every position of a number and concats them
#for example 9119 should output 811181
value = int(input("Enter value : "))
def squ(value):
    a = list(str(value))
    out = ""
    for i in range(0,len(a)):
        pow = int(a[i])*int(a[i])
        out = out + str(pow)
    print(out)
    
squ(value)
