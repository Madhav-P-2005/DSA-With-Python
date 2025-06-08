# Q8) Check wheather a Number is Strong or Not ? (example :- 145  :-  1! + 4! + 5! =>  145)   --> My Logic 

Number = int(input("Enter your Number :- "))
temp = abs(Number)
sum = 0 

while temp!=0:
    remainder = temp%10
    f=1 # Reset factorial for each digit

    i=1
    while i<=remainder:
        f = f * i
        i+=1

    sum = sum + f
    temp = temp//10

if Number==sum:
    print(f"{Number} is a Strong Number")
else:
    print(f"{Number} is not a Strong Number ")


'''

Output :- 

Enter your Number :- 145
145 is a Strong Number

'''



# Q8) Check wheather a Number is Strong or Not Using For - Loop ?   --> My Logic 

Number = int(input("Enter your Number :- "))
temp = abs(Number)
sum = 0 


for i in str(Number):
    remainder = temp%10
    f = 1 

    for i in range(1, remainder+1):
        f = f * i

    sum = sum + f 
    temp = temp//10


if sum==Number:
     print(f"{Number} is a Strong Number")
else:
    print(f"{Number} is not a Strong Number ")



'''

Output :- 

Enter your Number :- 1
1 is a Strong Number

'''



# Q8) Check wheather a Number is Strong or Not Using Do - While Loop ?   --> My Logic 

Number = int(input("Enter your Number :- "))
temp = abs(Number)
sum = 0 


while True :
    if temp!=0:
        remainder = temp%10
        f = 1 
        i=1

        while i<=remainder:
            f = f * i
            i+=1
        sum = sum + f
        temp = temp//10
    else:
        if(temp==0):
            break

if Number==sum:
    print(f"{Number} is a Strong Number")
else:
    print(f"{Number} is not a Strong Number")


'''

Output :- 

Enter your Number :- 0
0 is a Strong Number

'''




# Q8) Check wheather a Number is Strong or Not Using Functions  ?   --> My Logic 

def factorial(remainder):
     f=1
     i=1 
     while i<=remainder:
         f = f * i
         i+=1
     return f

def Check_Strong(Number):
    temp = abs(Number)
    sum=0

    while temp!=0:
          remainder = temp%10
          sum = sum + factorial(remainder)
          temp = temp//10
    return sum


Number = int(input("Enter your Number :- "))
if Number==Check_Strong(Number):
    print(f"{Number} is a Strong Number")
else:
    print(f"{Number} is not a Strong Number")


'''

Output :-

Enter your Number :- 200
200 is not a Strong Number

'''