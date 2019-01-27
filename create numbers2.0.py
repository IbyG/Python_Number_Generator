from random import*


question = input("would you like to start (y or n)?")


	
def makelines(num2, num1):
	while num2 > 0:
		#print("\n")
		producenumbers(num1)
		print("\n")
		num2 = num2 - 1
		
		
def producenumbers(num1):
	while num1 > 0:
		print(str(randint(0,9)), end="")
		num1 -= 1 
		
		

while question == "y" or question == "Y":
	num2 = int(input("how many to create: "))
	num1 = int(input("how many digits do you want: "))
	makelines(num2, num1)
	question = input("would you like to start (y or n)? ")