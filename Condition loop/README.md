# Loops
1. What is the diffrence between = and ==
= is an asignmenet operator while == is a comparison operator

2. Can i leave out the collon in an if, while, or for statement? yes/No
No 

3. Should i Use tab character to indent my code? Yes/No
Yes

4. Compose a program that takes three integers comand line arguments and writes 'equal' if all three are equal, and 'not equal' otherwise
a = input("Enter value a: ")
b = input("Enter value b: ")
c = input("Enter value c: ")
if a == b == c:
    print('equal')
else: 
    print('not equal')

5. what is th e value of j after each of the following code fragments is executed
a. j = 0
    for i in range(0, 10):
        j += i
value of J is 45

b. j = 1
    for i in range(0, 10):
        j += j

value of J is 1024

c. for j in range(0, 10):
    j += j

value of J is 18

6. what are m and n after the following code is executed?
n = 123456789
m = 0
while n != 0:
    m = (10 * m) + (n % 10)
    n //= 10

the value of m is 987654321
the value of n is 0