# Q14) Find the GCD(Greatest Common Factor)(HCF) of Two Numbers Using While loop ? (Euclid’s Algorithm)  --> My Logic 

Number1 = int(input("Enter your 1st Number :- "))
Number2 = int(input("Enter your 2nd Number :- "))
Temp = 0

while Number2!=0:
    Temp = Number2
    Number2 = Number1%Number2
    Number1 = Temp

print(f"GCD of {Number1} and {Number2} is  :- ",Number1)     


'''

Output :- 

Enter your 1st Number :- 10
Enter your 2nd Number :- 12
GCD of 10 and 12 is :-  2

'''



# Q14) Find the GCD(Greatest Common Factor)(HCF) of Two Numbers Using For - loop ?   --> My Logic 

Number1 = int(input("Enter the  1st  Number :- "))
Number2 = int(input("Enter the  2nd  Number :- "))
Temp = 0
i=1

for i in range(1, min(Number1 , Number2 +1)):
    if Number1%i ==0:
        if Number2%i==0:
               Temp = i
       
print(f"GCD of {Number1} and {Number2} is :- ", Temp)


'''

Output :- 

Enter the  1st  Number :- 10
Enter the  2nd  Number :- 1
GCD of 10 and 1 is :-  1

'''



# Q14) Find the GCD(Greatest Common Factor)(HCF) of Two Numbers Using Function  ?    --> My Logic 

def isGCD(Number1 , Number2):
    Temp = 0
    while Number2!=0:
        Temp = Number2
        Number2 = Number1%Number2
        Number1 = Temp
    return Number1

Number1 = int(input("Enter your 1st Number :-  "))
Number2 = int(input("Enter your 2nd Number :- "))
print(f"GCD of {Number1} and {Number2} is :- ",isGCD(Number1 , Number2))
    

'''

Output :- 

Enter your 1st Number :-  8
Enter your 2nd Number :- 16
GCD of 8 and 16 is :-  8

'''




# Q14) Find the GCD(Greatest Common Factor)(HCF) of Two Numbers Using Recursive Function  ?   --> My Logic 

def isGCD(Number1 , Number2):
     if Number2==0:
        return  Number1
     else:
          return isGCD(Number2 , Number1%Number2) 
     

Number1 = int(input("Enter the  1st  Number :- "))
Number2 = int(input("Enter the  2nd  Number :- "))
print(f"GCD({Number1}, {Number2}) = {isGCD(Number1, Number2)}")


'''

Output :- 

Enter the  1st  Number :- 10
Enter the  2nd  Number :- 20
GCD(10, 20) = 10

'''