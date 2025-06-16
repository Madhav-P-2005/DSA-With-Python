# Q12) Check wheather a Number is Even or Odd Using Nested if Condition ?   --> My Logic 
Number = int(input("Enter any Number :-  "))


if Number==0:
    print(f"{Number} is neither a Even or Odd Number")
    if(Number%2==0):
            print(f"{Number} is an Even Number")
    else:
            print(f"{Number} is an Odd Number")
else:
       print("Its an Invalid Number to Check ! ⚠️")


'''

Output:- 

Enter any Number :-  -34
Its an Invalid Number ! ⚠️

'''



# Q12) Check whether a list of numbers and bifurcate them into evens and odds using While Loop  ?   --> My Logic 

Even_List = []
Odd_List  = [] 
List = []
i = 0
j=0
Limit = int(input("Enter your Limit :- "))
while i<Limit:
   Number = int(input(f"Enter your {Limit}[{i}] :- "))
   List.append(Number)
   i+=1
while j<len(List):
     if List[j]%2==0:
        Even_List.append(List[j])
     else:
         Odd_List.append(List[j])
     j+=1
      

print("Even Numbers are :- ",Even_List)
print("Odd Numbers are :- ",Odd_List)


'''

Output :- 

Enter your Limit :- 4
Enter your 4[0] :- -2
Enter your 4[1] :- -4
Enter your 4[2] :- 6
Enter your 4[3] :- 7
Even Numbers are :-  [-2, -4, 6]
Odd Numbers are :-  [7]


'''



# Q12) Check whether a list of numbers and bifurcate them into evens and odds Using For Loop  ?   --> My Logic 

Even_List = []
Odd_List = []
i=0
j=0
List = []
Limit = int(input("Set Your Limit :- "))
for i in range(0, Limit):
    Number  = int(input(f"Enter your {Limit}[{i}] :- "))
    List.append(Number)
    i+=1

for j in range(len(List)):
    if List[j]%2==0:
        Even_List.append(List[j])
    else:
        Odd_List.append(List[j])
    j+=1


print("Even Numbers are :- ",Even_List)
print("Odd Numbers are :- ",Odd_List)


'''

Output :- 

Set Your Limit :- 0
Even Numbers are :-  []
Odd Numbers are :-  []

'''




# Q12) Check whether a list of numbers and bifurcate them into evens and odds using functions ?   --> My Logic 

def Appended_List():
    List = []
    i = 0
    Limit = int(input("Set Your Limit :- "))
    while i<Limit:
        Number  = int(input(f"Enter your {Limit}[{i}] :- "))
        List.append(Number)
        i+=1
    return List

def Check_Even_Or_Odd(List):
    Even_List = []
    Odd_List = []
    j = 0
    while j<len(List):
      if List[j]%2==0:  
        Even_List.append(List[j])
      else:
        Odd_List.append(List[j])
      j+=1
    return Even_List,Odd_List



Even_List , Odd_List = Check_Even_Or_Odd(Appended_List())
print("Even Numbers are :- ",Even_List)
print("Odd Numbers are :- ",Odd_List)


'''

Output :- 

Set Your Limit :- 5
Enter your 5[0] :- 1 
Enter your 5[1] :- 3
Enter your 5[2] :- 4
Enter your 5[3] :- 5
Enter your 5[4] :- 7
Even Numbers are :-  [4]
Odd Numbers are :-  [1, 3, 5, 7]

'''