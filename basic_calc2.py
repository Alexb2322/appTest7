#Basic Calc2 to junior users
#Developer: Alex Basante

#Libraries#########################
import os
###################################


#Funtions#########################
def calc(x, y):
    suma= x + y
    print("La suma es: ", suma)
    
#Main#########################   
os.system("clear") 
print("Press number 1: ")
a=int(input())

b=int(input("Presss number 2: "))

calc(a,b)