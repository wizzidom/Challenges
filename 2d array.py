#Myxzptlk
#This program will display a 2 dimentional array int rows and columns and find the total for each row

arrNumbers = [[1,3,9,8,34],[324,6,34,7,2],[4,4,3,5,7],[1,2,3,4,5]]
title = ''
for i in range(0,5):
    title = title + "Column" + str(i+1) + ' '
print(title + ' ' + "Total")
for irow in range(0,4):
	sline = ""
	rtotal = 0
	for icol in range(0,5):
		sline = sline + str(arrNumbers[irow][icol])+'	'
		rtotal = rtotal + arrNumbers[irow][icol]
	print(sline +' '+ str(rtotal))
