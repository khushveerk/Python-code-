
#
name=input("enter a name")
try:
    if name.isalpha():
        print("the name is correct")
    else:
        raise Exception("the name is not correct")
except Exception as e:
    print(e)
        



#
t1 =(1,4,6,3,2,8,5,10,9,7,6)

t2 =(12,15,11)
concatenate=(t1,t2)
print("tuple with concatenation",concatenate)





#
t1 =(1,4,6,3,2,8,5,10,9,7,6)
even_number=tuple(filter(lambda x: x%2==0,t1))
print("tuple with even numbers is",even_number)



#
t1 =(1,4,6,3,2,8,5,10,9,7,6)

half_value=len(t1)//2
first_half=t1[ :half_value]
print("first_half",first_half)
second_half=t1[half_value : ]
print("second_half",second_half)


#

def cubes():
    newlist=[]
    number=[1,2,6,3,"one"]
    for i in number:
        if type(i)==int:
            if i%2==0:
                newlist.append(i**3)
    print(newlist)
cubes()



#
def cubes():
    dict={}
    for i in range (1,5):
        dict[i]=i**3
    print(dict)
cubes()


#
string="hello world to python"
print(string[3:len(string)])
print(string[ :0])


#
string="hello world to python"
character =input("enter the character")
f=0
for i in string:
    if i ==character:
        f+=1
print("frequency of ", character,"is",f)



#
str1=input("enter the first string")
str2=input("enter the second string")
n1=int(input("enter the no of characters to be swap:"))

n=str1[ :n1]
m=str2[ :n1]

if n1<=min(len(str1),len(str2)):
       print(str1.replace(n,m))
else:
    print(str2.replace(n,m))



#
charac=input("enter the data")
if charac>'A' and charac<'Z':
    print(charac,"is a uppercase letter")
elif charac> 'a' and charac<'z':
    print(charac, "is a lowercase letter")
elif charac>'0' and charac<'9' :
    print(charac, "is a numeric digit")
else:
    print(charac, "is a special character")




#
def print_pyramid (n):
    for i in range(n):
        print(' '*(n-i-1),end='')
        print('*'*(2*i+1))
rows =5
print("pyramid")
print_pyramid(rows)

def print_reverse_pyramid (n):
    for i in range(n,0,-1):
        print(' '*(n-i),end='')
        print('*'*(2*i-1))
rows =5
print("pyramid")
print_reverse_pyramid(rows)










#
n=int(input("enter value"))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)  




#
n=int(input("enter value"))
count=0
num=2
while count<n:
    for i in range (2,num):
        if num %i==0:
            num+=1
            break
    else:
        print(num,end=',')
        count+=1
        num+=1





#
n=int(input("enter value"))
for num in range(1,n):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num,end=',')






#
n=int(input("enter the value"))
if n>1:
    for i in range (2,n):
        if n%i==0:
            print(n, "not a prime number ")
            break
    else:
        print(n,"is  a prime number")
         
else:
    print(n,"is not prime number")





#
n =int(input("enter value ")) 

if n>1:
   
   for i in range(2,n):
   
    if n % 10:
   
     print(n, "not a prime number") 
  
     break

   else:
   
    print(n, "prime number") 

else: 
   
   print(n, "not a prime number ")











#
a= int(input("enter the value of a"))
b= int(input("enter the value of b"))
c= int(input("enter the value of c"))

d= b**2 -4*a*c
r1=(-b+(d)**0.5)/2*a
r2= (-b-(d)**0.5)/2*a
if d>=0:
  print("the real roots are",r1,r2)
    
else:
  print("there are no real roots")  
