# Q9) Find the Factorial of a Number using While Loop ?  (Example :- 5 => 5*4*3*2*1 => 120)    --> My Logic 

Number = int(input("Enter any Number :- "))
f = 1 
i = 1 

while i<=Number:
      if Number==0:
        print(f" Factorial of {Number} is  :-  ",i)
        break
      f = f * i
      i+=1

print(f"Factorial of {Number} is :- ",f)


'''

Output :-

Enter any Number :- 5
Factorial of 5 is :-  120

'''



# Q9) Find the Factorial of a Number using For-Loop ?      ---> My Logic 

Number = int(input("Enter any Number :- "))
f = 1 
i = 1 

for i in range(1 , Number+1):
    if i<=Number:
        f = f * i

print(f"Factorial of {Number} is :- ",f)


'''

Output :- 

Enter any Number :- 0
Factorial of 0 is :-  1

'''



# Q9) Find the Factorial of a Number using Do - While - Loop ?      ---> My Logic 

Number = int(input("Enter any Number :- "))
f = 1
i = 1 


if Number==0:
       f = 1 
else:
    while True:
      f = f * i
      i+=1
      if i > Number:
           break
       
print(f"Factorial of {Number} is :- ",f)


'''

Output :- 

Enter any Number :- 4
Factorial of 4 is :-  24

'''




# Q9) Find the Factorial of a Number using Function ?       ---> My Logic 


def Check_Factorial(Number):
     f = 1
     i = 1
     while(i<=Number):
          if Number==0:
               print(i)
          f = f * i
          i+=1
     return f
     

Number = int(input("Enter any Number :- "))
print(f"Factorial of {Number} is :- ",Check_Factorial(Number))



'''

Output :- 

Enter any Number :- 1
Factorial of 1 is :-  1

'''