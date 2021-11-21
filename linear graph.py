#By myxzptlk
import random
# y = mx + c
# this program will help you draw linear graphs by calculating the x and y - intercepts and any other point on the graph

m = int(input("Enter value of m: ")) #gradient
c = int(input("Enter value of c: "))# verical shift
#X-intercepts
xi = -c/m
#y - intercept
yi = c
#Other point
y = m * random.randint(1,5) + c
x = (y - c)/m
print("Y-intercept: (0;" + str(yi)+")")
print("X-intercept: ("+str(xi)+";0)")
print("Other point: (" + str(x) +";"+ str(y)+")")
#Will soon release an update of this program that sketches the graph for you



