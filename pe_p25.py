# Project Euler Problem 25

# Problem Brief:
#    Determine which term in Fibonacci sequence is
#    the first to have 1000 digits

# Source:
#   Brian Puthuff
#   2015.04.01

# function to get next fibonacci number
def next_fib(a = [], f_one = [], f_two = []):
	carry, sum = 0, 0
	for i in range(999, -1, -1):
		sum = f_one[i] + f_two[i] + carry
		carry = 0
		if(sum > 9):
			carry = 1
			sum = sum % 10
		a[i] = sum
	
	for i in range(999, -1, -1):
		f_one[i], f_two[i] = f_two[i], a[i]

# main sequence

# create lists
next_term = []
fib_term1 = []
fib_term2 = []
 
# term count variable
term = 3
 
# initialize lists
for i in range(0, 1000, 1):
	next_term.append(0)
	fib_term1.append(0)
	fib_term2.append(0)

# starting term
fib_term1[999], fib_term2[999] = 1, 2
while(next_term[0] == 0):
	next_fib(next_term, fib_term1, fib_term2)
	term = term + 1

# print term
print('\n')
print("Term: %s" %term)

# print 1000 digit number (for fun)
print("The %s term in the Fibonacci sequence is:" %term)
for i in next_term:
	print(i, end = '')
print('\n')

