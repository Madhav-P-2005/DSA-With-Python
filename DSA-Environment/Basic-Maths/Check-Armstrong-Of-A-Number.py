# Q5) Check Wheather a Number is Armstrong or Not  Using While Loop ? Example :- 371 =>   3³  + 7³  + 1³  => 371  --> My Logic 

Number = int(input("Enter your Number :- "))
temp = abs(Number)
Total = 0
num_digits = len(str(Number))  

while temp != 0:
    remainder = temp % 10
    Total += pow(remainder, num_digits)
    temp = temp // 10

if Total == Number:
    print(f"{Number} is an Armstrong Number")
else:
    print(f"{Number} is not an Armstrong Number")


'''

Output :- 

Enter your Number :- 371
371 is an Armstrong Number

'''


# Q5) Check Wheather a Number is Armstrong or Not  Using For Loop ?  --> My Logic 

Number = int(input("Enter your Number :- "))
temp = abs(Number)
Total = 0
num_digits = len(str(Number))  

for i in str(temp):
    if temp==0:
        break
    else:
         Total = Total + pow(int(i), num_digits)

if(Total==Number):
   print(f"{Total} is a Armstrong Number")
else:
   print(f"{Total} is not a Armstrong Number")


'''

Output :-

Enter your Number :- 0
0 is a Armstrong Number

'''


# Q5) Check Wheather a Number is Armstrong or Not  Using While Loop ?   --> My Logic 

Number = int(input("Enter your Number :- "))
temp = abs(Number)
Total = 0
num_digits = len(str(Number))  

while True:
    if temp>0:
        remainder = temp%10
        Total = Total + pow(remainder, len(str(Number)))
        temp = temp//10 
    else:
        break
    

if(Total==Number):
    print(f"{Total} is a Armstrong  Number ")
else:
    print(f"{Total} is not a Armstrong Number")


'''

Output :- 

Enter your Number :- 52
29 is not a Armstrong Number

'''



# Q5) Check Wheather a Number is Armstrong or Not  Using While Loop ?  --> My Logic 

def Check_Armstrong(Number):
    temp = abs(Number)
    Total = 0
    num_digits  = len(str(Number))

    while temp>0:
        remainder = temp%10
        Total = Total + pow(remainder , num_digits)
        temp = temp//10

    return Total==Number


Number = int(input("Enter your Number :- "))
if(Check_Armstrong(Number)):
    print(f"{Number} is a Armstrong Number ")
else:
    print(f"{Number} is not a Armstrong Number")


'''

Output :-

Enter your Number :- -407
-407 is not a Armstrong Number

'''




# Anirudh Sir's Approach  & (GFG Solved) :-   
class Solution:
    def armstrongNumber (self, n):
        # code here 
        nod = len(str(n))
        temp = n
        armstrong = 0
        while temp!=0:
               remainder = temp % 10 
               armstrong = armstrong + (remainder**nod)
               temp = temp // 10
        return armstrong==n
    


# Time Complexity  :-   T(n) = O(log10​(x))
# Space Complexity :-   S(n) = O(1)    or  O(log x)   