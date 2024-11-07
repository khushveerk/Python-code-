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

### a. Check if 'n' is prime or not.
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

### b. Generate all prime numbers till 'n'

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

### c. generate first 'n' prime numbers

n =eval(input("enter value ")) 

count = 0
number = 2
while count < n:
   for i in range(2,number):
      if number % i == 0:
       number += 1
       break
   else:
      print(number, end=',')
      count+= 1
      number+= 1

![Screenshot 2024-11-07 131319](https://github.com/user-attachments/assets/019f4a6a-8baf-4254-ae80-0cc8b9ba443f)





## practical 3 - WAP to create a pyramid of the character '*' and a reverse pyramid.



def print_pyramid(n):
   
   for i in range(n):
     
     print(' ' * (n - i - 1), end='')
     
     print('*' * (2 * i + 1))

#Number of rows for the pyramid
rows = 5

print("Pyramid:")

print_pyramid(rows)


def print_reverse_pyramid(n):
   
   for i in range(n, 0, -1):
    
     print(' ' * (n - i), end='')
    
     print('*' * (2 * i - 1))

#Number of rows for the reverse pyramid
rows = 5

print("\nReverse Pyramid:")

print_reverse_pyramid(rows)

![IMG-20241106-WA0009](https://github.com/user-attachments/assets/00f62032-1d63-4650-902e-1fa292b5f22f)

![IMG-20241106-WA0008](https://github.com/user-attachments/assets/88de3a7a-4f38-4621-a542-bd7bed445a53)





## practical 4 - WAP that accepts a character and performances the following.

### a. print whether the character is a letter or numeric digit or a special character. 

### b. if the character is a letter, print whether the letter is uppercase or lowercase. 

### c. if the character is numeric digit, print its name in the text.

  
charac = input("Enter the data: ")

if charac >= 'A' and charac <= 'Z':
    
   print(charac, "is an Uppercase Letter")

elif charac >= 'a' and charac <= 'z':
    
   print(charac, "is a Lowercase Letter")

elif charac >= '0' and charac <= '9':
    
   print(charac, "is a Numeric Digit")
   n = int(charac)
   
   dict= {0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine'}
    
   print(dict[n])

else:

   print(charac, "is a Special Character")   

   
![IMG-20241106-WA0011](https://github.com/user-attachments/assets/532abd9e-cfa7-4fd0-aa49-4ac96f3a142f)


![IMG-20241106-WA0010](https://github.com/user-attachments/assets/af3bf10a-22b0-41d2-bb60-c8e6d3c881b9)
    
   


## practical 5 - WAP to swap the first n characters of two strings .

str1 =input("enter first string ")

str2 =input("enter second string ")

n1 =int(input("enter no of characters which is to be swap: "))

n=str1[ :n1]

m=str2[ :n1]

if n1 <= min(len(str1),le(str)):
  
  print(str1.replace(n,m))

else:
  
  print(str2.replace(n,m))


![image](https://github.com/user-attachments/assets/48b4bf0b-3c93-458d-8906-9df8854dfe5d)





## practical 6 - WAP to 

print("Enter the first string:", end="")

string1 =input()

print("Enter the second string:", end="")

string2 =input()

print("\nstring before swap: ")

print(" string1 =", string1)

print(" string2 =", string2)

temp = string1 

string1 = string2

string2 = temp

print("\nstring before swap: ")

print(" string1 =", string1)

print(" string2 =", string2)



![IMG_20241106_115748_028](https://github.com/user-attachments/assets/bac06745-7b54-4056-84ee-a461fb68ec19)



## practical 7 - WAP to perform the following operations on a string. 

### a. find the frequency of a character in a string . 

string = "hello world to python"

character = input("enter a character ")

f=0

for i in string:

   if i ==character:
     f+=1
print("frequency of" , character ,'is', f)     

![Screenshot 2024-11-07 112630](https://github.com/user-attachments/assets/965af336-aee9-43b1-885f-93e89f10e10f)



### b. replace a character by another character in a string .

string = "hello world to python"

print(string.replace ("e","i"))


![Screenshot 2024-11-07 113427](https://github.com/user-attachments/assets/5480e2ce-5bf2-48cf-98c9-c3da63472fec)



### c. remove the first occurance os a character from a satring .

string = "hello world to python program"

print(string[3:len(string)])

![Screenshot 2024-11-07 114106](https://github.com/user-attachments/assets/64a834c4-7768-4cf8-93a3-5ab1705db93e)



### d. remove all the occurances of a character from a string

string = "hello world to python tutorial"

print(string[ :0])

![Screenshot 2024-11-07 114402](https://github.com/user-attachments/assets/636c507d-7afc-4e33-ae1c-4fe52059df51)


print(string[ :2])


![Screenshot 2024-11-07 114538](https://github.com/user-attachments/assets/9df7d84a-bd5e-4c58-a7f0-028ada7db6bb)














