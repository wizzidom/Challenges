#Given a list of identical numbers and one unidentical number, the program shall expose the alien number
a = [1,1,3,1,1]
for i in range(0,len(a)):
	if (a.count(a[i]) > 1):
		continue
	else:
		print(a[i])
