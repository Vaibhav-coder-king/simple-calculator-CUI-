import pyfiglet
print(pyfiglet.figlet_format("The Simple Calculator",font="slant"))

def spac():
	print('\n')
	
def inpt(value):
	a=float(input(f'enter the {value}='))
	return a
	
def even(n):
	if n%2==0:
		return 'even'
	else:
		return 'odd'

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
    
def fact(n):
	fact=1
	for i in range(n,0,-1):
		fact*=n
	return fact
while True:
	print("the following are option in simple calculator:-\n1 for Addtion(+)\n2 for Subraction(-)\n3 for Multiplication(×)\n4 for Division(÷)\n5 for Finding power\n6 for Finding Remainder.\n7 for Check number is even or odd.\n8 for Check Number is prime or not.\n9 for Finding Factorial\n10 for exit")
	ch=input("enter your choice🤔=")
	try:	
		if ch=='1':
			n=int(input('🤔\nhow many digits do you want to add:'))
			sum=0
			for i in range(n):
				sum+=inpt(f'num{i+1}')
			print(f'The sum of given numbers are {sum}')
			spac()
			
		elif ch=='2':
			n1=inpt('num1')
			n2=inpt('num2')
			sb=n1-n2
			print(f'The result after subtracting {n2} from {n1} is {sb}.')
			spac()
			
		elif ch=='3':
			n=int(input('🤔\nhow many digits do you want to multiply:'))
			mul=1
			for i in range(n):
				mul*=inpt(f'num{i+1}')
			print(f'The multiply of given numbers are {mul}')
			spac()
			
		elif ch=='4':
			n1=inpt('num1')
			n2=inpt('num2')
			q=input('🤔\ndo you want to result in decimal(y/n)?=').lower()
			if q=='y':
				divide=n1/n2
				print(f'The result after dividing {n2} from {n1} is {divide}.')
			elif q=='n':
				divide=n1//n2
				print(f'The result after dividing {n2} from {n1} is {divide}.')
			else:
				print(f'Invalid input{'!'*11}')
			spac()
			
		elif ch=='5':
			b=inpt('base value')
			p=inpt('power value')
			print(f'The result of {b}^{p} is {b**p}.')
			spac()
			
		elif ch=='6':
			n1=inpt('num1')
			n2=inpt('num2')
			divide=n1%n2
			print(f'The remainder after dividing {n2} from {n1} is {divide}.')
			spac()
			
		elif ch=='7':
			num=inpt('number')
			print(f'The number {num} is {even(num)}.')
			spac()
		
		elif ch=='8':
			number = int(input("Enter a number: "))
			if is_prime(number):
				print(f"{number} is a prime number.")
			else:
				print(f"{number} is not a prime number.")
			spac()
			
		elif ch=='9':
			num=int(inpt('number'))
			print(f'the factorial of {num} is {fact(num)}.')
			spac()
			
		elif ch=='10':
			break
			
		else:
			print(f'Invalid input{'!'*11}')
			spac()
			
	except:
		print(f'Invalid input{'!'*11}')
		spac()
print(pyfiglet.figlet_format("Bye-Bye"))