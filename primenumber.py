list1=[]
number=int(input("Please enter your number:"))
for i in range(1,number+1):
  if number %i ==0:
     list1.append(i)
if len(list1) >2:
   print(f"Your number{number} is not prime number")    
else:
   print(f"Your number {number} is prime number")