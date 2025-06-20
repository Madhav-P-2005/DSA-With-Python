# Q15) Find the LCM (Lowest Common Multiple) of two Numbers Using while Loop ?   --> My Logic 

Number1 = int(input("Enter your 1st Number :- "))
Number2 =  int(input("Enter your 2nd Number :- "))
Result = 0

Start  = max(Number1 , Number2)

while Start!=0:
    if Start%Number1==0:
         if Start%Number2==0:
              Result = Start
              break
    Start+=1 


print(f"LCM of {Number1} and {Number2} is :- ",Result)
        

'''

Output :- 

Enter your 1st Number :- 4
Enter your 2nd Number :- 6
LCM of 4 and 6 is :-  12

'''


# OR

# Using Ternary Operator ! 

Number1 = int(input("Enter your 1st Number :- "))
Number2 =  int(input("Enter your 2nd Number :- "))
LCM = 0

Start =  Number1 if Number1>Number2 else Number2 

while Start!=0:
       if Start%Number1==0:
            if Start%Number2==0:
                LCM = Start
                break
       Start+=1



print(f"LCM of {Number1} and {Number2} is :- ", LCM)



'''

Output :- 

Enter your 1st Number :- 1
Enter your 2nd Number :- 2
LCM of 1 and 2 is :-  2

'''



# Q15) Find the LCM (Lowest Common Multiple) of two Numbers Using while Loop ?   --> My Logic 

Number1 = int(input("Enter your 1st Number :- "))
Number2 =  int(input("Enter your 2nd Number :- "))
Result = 0

for Start in (Start , max(Number1, Number2 + 1)):
     if Start%Number1==0 and Start%Number2==0:
          LCM = Start
          break
     Start+=1


print(f"LCM of {Number1} and {Number2} is :- ",LCM)  


'''

Output :- 

Enter your 1st Number :- 0
Enter your 2nd Number :- 1
Traceback (most recent call last):
  File "e:\DSA with Python\DSA-Environment\Basic-Maths\Find-LCM-Of-Two-Numbers.py", line 69, in <module>
    Number2 =  int(input("Enter your 2nd Number :- "))
            ^^^^^^^^^^^^^
ZeroDivisionError: integer modulo by zero

'''



# Q15) Find the LCM (Lowest Common Multiple) of two Numbers Using Functions ?   --> My Logic 


def get_Numbers():
     Number1 = int(input("Enter your 1st Number :- "))
     Number2 =  int(input("Enter your 2nd Number :- "))  
     return Number1, Number2


def Maximum(Number1 , Number2):
    if Number1>Number2:
         return Number1
    else:
         return Number2
         
     

def isLCM(Number1 , Number2):
    
       Start = Maximum(Number1 , Number2)
       LCM = 0 

       while Start!=0:
           if Start%Number1==0:
                if Start%Number2==0:
                     LCM = Start
                     break
           Start+=1
        
       return LCM

     
Number1 , Number2 = get_Numbers()
Result = isLCM(Number1, Number2)
print(f"LCM of {Number1} and {Number2} is :- ",Result)
           


'''

Output :- 

Enter your 1st Number :- 5 
Enter your 2nd Number :- 8
LCM of 5 and 8 is :-  40

'''