# Q7) Calculate the sum of digits of a Number using While Loop ?   --> My Logic 

Number = int(input("Enter your Number :- "))
temp = abs(Number)
sum = 0

while temp!=0:
    remainder = temp%10
    sum = sum + remainder
    temp = temp//10

print(f"The Sum of digits of {Number} is :- ",sum)



'''

Output :- 

Enter your Number :- 123
The Sum of digits of 123 is :-  6

'''




# Q7) Calculate the sum of digits of a Number using For Loop  ?   --> My Logic 

Number = int(input("Enter your Number :- "))
temp = abs(Number)
sum = 0

for i in str(abs(temp)):
            sum = sum + int(i)

print(f"The Sum of digits of {Number} is :- ",sum)


'''

Output :- 

Enter your Number :- 0
The Sum of digits of 0 is :-  0

'''




# Q7) Calculate the sum of digits of a Number using Do-While Loop ?   --> My Logic 

Number = int(input("Enter your Number :- "))
temp = abs(Number)
sum = 0

while True:
        remainder = temp%10
        sum+=remainder
        temp=temp//10
        if(temp==0):
                break


print(f"The Sum of digits of {Number} is :- ",sum)



'''

Output :- 

Enter your Number :- 0891
The Sum of digits of 891 is :-  18

'''




# Q7) Calculate the sum of digits of a Number using Functions ?     --> My Logic 

def Sum_of_Digits(Number):
    temp = abs(Number)
    sum=0

    while temp!=0:
           remainder = temp%10
           sum+=remainder
           temp=temp//10       
    return sum


Number = int(input("Enter your Number :- "))
print(f"The Sum of digits of {Number} is :- ",Sum_of_Digits(Number))


'''

Output :- 

Enter your Number :- 1001
The Sum of digits of 1001 is :-  2

'''