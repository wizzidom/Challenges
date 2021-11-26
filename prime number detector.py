#Myxzptlk
#Prime number dectetor
n = int(input("Enter a number: "))
icount = 0
if n == 1:
    print("This number is neither a prime nor composite number")
else:
    for i in range(1,n+1):
            if n % i == 0:
                    icount += 1
            else:
                    continue
    if icount > 2:
            print("Not prime")
    else:
            print("Prime")

