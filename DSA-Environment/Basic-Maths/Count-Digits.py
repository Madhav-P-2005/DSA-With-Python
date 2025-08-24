# 2) Count Digits Using while - Loop ?   ---> My Logic

Number = int(input("Enter any value :-  "))
temp = abs(Number)    # abs() :- Copies only the magnitude (i.e., makes it positive)
count = 0

if temp==0:
      count+=1
else: 
    while temp>0:
        temp = temp//10
        count+=1


print(f"Total digits in {Number} using while is :- ",count)


'''

Output :- 

Enter any value :-  2987
Total digits in 2987 using while is :-  4

'''


# 2) Count Digits Using for - loop ?   ---> My Logic   (Note :- # ⚠️ Using for is not natural here..)

Number = int(input("Enter any value :-  "))
temp = abs(Number)   
count = 0

if temp==0:
        count=1
else:
      for _ in range(100):
                   if temp>0:
                        temp = temp//10
                        count+=1


print(f"Total digits in  {Number} using for-loop is :- ",count)


'''

Output :-

Enter any value :-  00
Total digits in  0 using for-loop is :-  1

'''


# 2) Count Digits  Using  do - While  loop ?   ---> My Logic

Number = int(input("Enter any value :-  "))
temp = abs(Number)   
count = 0


while True:
    count+=1
    temp = temp//10
    if temp==0:
        break


print(f"Total digits in  {Number} using do-while is :- ",count)


'''

Output :- 

Enter any value :-  0
Total digits in  0 using do-while is :-  1

'''



# 2) Count Digits  Using  Function ?   ---> My Logic

def CountNum(Number):
    temp = abs(Number)
    count = 0

    if temp == 0:
        return 1 
    
    while temp>0:
        temp = temp//10
        count+=1
        
    return count


Number = int(input("Enter any Value :- "))
Ans  = CountNum(Number)
print(f"Total digits in {Number} using function is :- ",Ans)


'''

Output :-

Enter any Value :- 1001
Total digits in 1001 using function is :-  4

'''



# Anirudh Sir's Approach :-

from math import *

def CountDigits(num):
      return int(log10(num) + 1)


num = int(input("Enter your Number/Integer :- "))
print(CountDigits(num))



'''

Output :- 

Enter your Number/Integer :- 3454365
7

'''


# Time Complexity :-  n = n//10   =>   O(log10(n))    
# Space Complexity :-  O(1)     