# Q4) Check wheather a Number is a Palindrome or Not Using While Loop ?   Example :-   1221  , 1001 , 101 etc..

Number  = int(input("Enter the Value :-  "))
reverse = 0
temp = abs(Number)

while(temp!=0):
    remainder  = temp%10
    reverse = reverse * 10 + remainder
    temp = temp//10


if(reverse==Number):
    print(f"{reverse} is a Palindrome Number ")
else:
    print(f"{reverse} is not a Palindrome Number")


'''

Output :- 

Enter the Value :-  121
121 is a Palindrome Number 

'''


# Q4) Check wheather a Number is a Palindrome or Not Using For - Loop  ?  # ⚠️ Not ideal use of for loop

Number  = int(input("Enter the Value :-  "))
reverse = 0
temp = abs(Number)

for i in range(temp):
    if(temp!=0):
        remainder = temp%10
        reverse = reverse * 10 + remainder
        temp = temp//10

if(reverse==Number):
    print(f"{reverse} is a Palindrome Number")
else:
    print(f"{reverse} is not a Palindrome Number")


'''

Output :- 

Enter the Value :-  1001
1001 is a Palindrome Number

'''


# Q4) Check wheather a Number is a Palindrome or Not Using Do - While Loop ?    --> My Logic 

Number  = int(input("Enter the Value :-  "))
reverse = 0
temp = abs(Number)

# Do-while simulation: run at least once
while True:
        remainder = temp%10
        reverse = reverse * 10 + remainder
        temp  = temp//10
        if(temp==0):
             break

if(reverse==Number):
    print(f"{reverse} is a Palindrome Number")
else:
    print(f"{reverse} is not a Palindrome Number")


'''

Output :- 

Enter the Value :-  0
0 is a Palindrome Number

'''


# Q4) Check wheather a Number is a Palindrome or Not Using Functions ?   --> My Logic 

def Check_Palindrome(Number):
    temp=abs(Number)
    reverse=0
    while(temp!=0):
        remainder = temp%10
        reverse = reverse * 10 + remainder
        temp = temp//10
    return reverse==Number


Number  = int(input("Enter the Value :-  "))
if Check_Palindrome(Number):
        print(f"{Number} is a Palindrome Number ")
else:
        print(f"{Number} is not a Palindrome Number ")


'''

Output :- 

Enter the Value :-  345
345 is not a Palindrome Number 

'''



# Anirudh's Sir's Approach :- 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        result = 0
        while temp > 0:
            remainder = temp % 10
            result = (result * 10) + remainder
            temp = temp // 10
        return result == x
    

# Time Complexity  :-   T(n) = O(log10​(x))
# Space Complexity :-   S(n) = O(1)    or  O(log x)   