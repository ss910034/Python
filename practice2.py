#!pythoon3
def Collatz(number):
	if number%2 == 0:
		number = number // 2
	else:
		number = 3 * number + 1
	return number

print("Enter number:")
try:
	x = int(input())
	while( x != 1 ):
		x = Collatz(x)
		print(x)
except ValueError:
	print("Please enter an integer number")
