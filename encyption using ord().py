#BY MYXZPTLK
#Encyption using ord() 
x = input("Enter text to encrypt: ")
encrypted = ''
for i in range(0,len(x)):
	encrypted = encrypted + str(ord(x[i])) + '#'
print(encrypted)

    

    



