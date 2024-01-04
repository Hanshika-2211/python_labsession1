# Aim : Write a program to demonstrate the following operators in  Python with example :

# Arithmetic operator:
# In this part the user enters the values for the four variables and calculate the final 
# value after solving the expression and store it in a variable named 'answer'
print("Q.) (a * (b + c) - d) / 2" )
print("Let's solve this expression")
a = int(input("Enter the value for 'a': "))
b = int(input("Enter the value for 'b': "))
c = int(input("Enter the value for 'c': "))
d = int(input("Enter the value for 'd': "))

answer = (a*(b+c)-d)/2
print("The answer for the above expression is =",answer)

# Relational operator:
# In this the relational operator will chec whether the answer is less than,greater than or equal to 0
# Respectively prints True or false value for the same.
greater = answer>0
less = answer<0
equal = answer==0

print("Result > 0:", greater)
print("Result < 0:", less)
print("Result == 0:", equal)

# Logical operator:
# In this the logical operater checks whether the answer is positive or negtaive or 0.
# And prints True or False accordingly.
if (answer == greater and answer != equal):
    print("Result is a positive integer.")
elif (answer ==less and answer != equal):
    print("Result is a negative integer.")
else:
    if (answer == equal):
         print ("Result is zero.")

# Assignment operator:

decimal = answer
print("The result is in decimal form so let's round it off,")
roundedoff = int(decimal + 0.5)

print("Original Decimal:", decimal)
print("Rounded Number:", roundedoff)

# Bit-wise operator:

number = roundedoff
if number <= 2:
    print('The program terminates here')
    exit()
else:
    numberstring = str(number)

x = str(number)
x1 = x[-2]
y1 = x[-1]
print("x =",x1)
print("y =",y1)

binary_x1 = bin(int(x1))[2:]
binary_y1 = bin(int(y1))[2:]

print("Binary representation of x1:", binary_x1)
print("Binary representation of y1:", binary_y1)
resultand = bin(int(x1) & int(y1))[2:]
resultor = bin(int(x1) | int(y1))[2:]
resultxor = bin(int(x1) ^ int(y1))[2:]
int_resultand = int(resultand, 2)
int_resultor = int(resultor, 2)
int_resultxor = int(resultxor, 2)

print("Result of Bitwise AND:",resultand,"i.e", int_resultand)
print("Result of Bitwise OR:",resultor,"i.e", int_resultor)
print("Result of Bitwise XOR:",resultxor,"i.e", int_resultxor)

# Ternary operator:

num1 = int_resultand
num2 = int_resultor
num3 = int_resultxor

greatestresult = (
    num1 if num1 >= num2 and num1 >= num3
    else num2 if num2 >= num3
    else num3
)
print("The greatest result among the integers:", greatestresult)
smallestresult = (
    num1 if num1 <= num2 and num1 <= num3
    else num2 if num2 <= num3
    else num3
)

print("The smallest result among AND, OR, and XOR is:", smallestresult)

# Membership operator:

n = greatestresult  
sequence = [i for i in range(n)]
print("Sequence up to", n, ":", sequence)

n = smallestresult  
sequence2 = [i for i in range(n)]
print("Sequence up to", n, ":", sequence2)

# Identity operator:

xn = sequence
print("x2 =", xn)
if xn is sequence:
    print("x2 and sequence refer to the same list.")
else:
    print("x2 and sequence do not refer to the same list.")

yn = sequence2
print("y2 =", yn)
if yn is xn:
    print("y2 and x2 refer to the same list.")
else:
    print("y2 and x2 do not refer to the same list.")