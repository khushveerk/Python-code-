# Python-code-
## practical 1 - WAP to find the roots of a quadratic equation.


a=int(input("Enter a: "))

b=int(input("Enter b: "))

c=int(input("Enter c: "))

d= b** 2-4*a*c 

   r1 =(-b + (d)**0.5)/2*a
   
   r2 =(-b - (d)**0.5)/2*a

if d>= 0:

   prinrt("The roots are real" , r1 ,r2)

else: 

   print(" roots are not real")
   

