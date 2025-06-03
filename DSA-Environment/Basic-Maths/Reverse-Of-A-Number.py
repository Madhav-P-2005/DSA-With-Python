# Q3) Reverse of a Number using While Loop ? --> My Logic

Number = int(input("Enter your Number :- "))
reverse = 0
temp = abs(Number)


while temp>0:
    remainder = temp%10
    reverse = reverse * 10 + remainder
    temp = temp//10

print(f"Reversed Number of {Number}  using While is  :- ",reverse)


'''

Output :- 

Enter your Number :- 2341
Reversed Number of 2341  using While is  :-  1432

'''



# Q3) Reverse of a Number using For - Loop ?   --> My Logic

Number = int(input("Enter your Number :- "))
temp = abs(Number)
reverse = 0

for i in range(temp):
    if temp>0:
        remainder = temp%10
        reverse = reverse * 10 + remainder
        temp = temp//10

print(f"Reverse of {Number} using for-loop is ",reverse)


'''

Output :- 

Enter your Number :- 90
Reverse of 90 using for-loop is  9

'''




# Q3) Reverse of a Number using Do - While Loop ?   --> My Logic

Number = int(input("Enter your Number :- "))
temp = abs(Number)
reverse  = 0 

if temp==0:
    reverse = 0
else:
    while True:
        remainder = temp%10
        reverse = reverse * 10 + remainder
        temp = temp//10
        if temp==0:
            break
        
print(f"Reversed Number of {Number} uding Do-while is :- ", reverse)


'''

Output :- 

Enter your Number :- 2000
Reversed Number of 2000 uding Do-while is :-  2

'''



# Q3) Reverse of a Number using Function ?  --> My Logic

def Reverse_Num(Number):
    temp = abs(Number)
    reverse = 0
    while temp>0:
        remainder  = temp%10
        reverse  = reverse * 10 + remainder
        temp = temp//10
    return reverse


Number = int(input("Enter your Number :- "))
Reversed_Number =Reverse_Num(Number)
print(f"Reversed Number of {Number} using Function is :- ",Reversed_Number)



'''

Output :- 

Enter your Number :- 980675
Reversed Number of 980675 using Function is :-  576089

'''