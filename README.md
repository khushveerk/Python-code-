# Python-code-
## practical 1 - WAP to find the roots of a quadratic equation.


a=int(input("Enter a: "))

b=int(input("Enter b: "))

c=int(input("Enter c: "))

d= b** 2-4*a*c 

   r1 =(-b + (d)**0.5)/2*a
   
   r2 =(-b - (d)**0.5)/2*a

if d>= 0:

   print("The roots are real" , r1 ,r2)

else: 

   print(" roots are not real")

![IMG-20241106-WA0005](https://github.com/user-attachments/assets/8112c4bc-faff-4f76-8d8e-383c53c203e0)

![IMG-20241106-WA0004](https://github.com/user-attachments/assets/f4c204ea-cc13-4349-b7b5-3d59429c9c77)


## practical 2 - WAP to accept a number 'n' to compute the following:

a. Check if 'n' is prime or not.
code= 

n =eval(input("enter value ")) 

if n>1:
   
   for i in range(2,n):
   
   if n % 10:
   
   print(n, "not a prime number") 
  
   break

else:
   
   print(n, "prime number") 

else: 
   
   print(n, "not a prime number ")

Output = 

enter value 1

1 not a prime number 

enter value 29 

29 prime number

b. Generate all prime numbers till 'n'

Code =

n= int(input("enter value")) 

for num in range(1,n): 
  
   if num > 1: 
   
   for i in range (2, num): 
       
    if num % i == 0: 
      
    break

 
   else: print(num, end=',')


Output enter value 100 2,3,5,7,11,13,17,19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,79,83,89,97,

![IMG-20241106-WA0007](https://github.com/user-attachments/assets/fa5f115c-003a-4b6a-a5e6-e5da76402c89)

![IMG-20241106-WA0006](https://github.com/user-attachments/assets/34b98eb9-3093-485d-b684-01582cbdeccd)

## practical 3 - WAP to create a pyramid of the character '*' and a reverse pyramid.

n= int
