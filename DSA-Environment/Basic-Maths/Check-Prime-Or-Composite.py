# Q13) Check Wheather a Number is Prime or Composite Using While and Do - While ?   --> My Logic 

Number = int(input("Enter any Number :- "))
count=0

if Number<=1:
    print(f"{Number} is neither Prime nor Composite")
else:
  i=1
  while i<=Number:
      if Number%i==0:
          count+=1
      i+=1


  if(count==2):
    print(f"{Number} is a Prime Number")
  else:
    print(f"{Number} is a Composite Number")


'''

Output :- 

Enter any Number :- 5090    
5090 is a Composite Number

'''


# Q13) Check Wheather a Number is Prime or Composite Using For - Loop ?   --> My Logic 

Number = int(input("Enter any Number :- "))
count=0

if Number<=1:
    print(f"{Number} is neither Prime nor Composite")
else:
   
   for i in range(1, Number+1):
       if Number%i==0:
           count+=1
           

   if(count==2):
      print(f"{Number} is a Prime Number")
   else:
     print(f"{Number} is a Composite Number")


'''

Output :- 

Enter any Number :- 0
0 is neither Prime nor Composite

'''



# Q13) Check Wheather a Number is Prime or Composite Using Functions ?   --> My Logic 

def Prime_Or_Composite(Number):
   if Number<=1:
      return "is neither Prime or Composite"
   else:
      count=0
      i=1
      while(i<=Number):
         if(Number%i==0):
               count+=1
         i+=1
      if count==2:
         return True
      else:
         return False
      

def Display(Number):
    result = Prime_Or_Composite(Number)
    if result=="is neither Prime or Composite":
       print(f"{Number} is neither a Prime or Composite Number")
    elif result:
       print(f"{Number} is a Prime Number")
    elif result:
       print(f"{Number} is a Composite Number")

   
Number  = int(input("Enter any Number :- "))
Display(Number)


'''

Output :- 

Enter any Number :- -435
-435 is neither a Prime or Composite Number

'''




# Q13) Check Wheather a Number is Prime or Composite and Bifercate them Using Lists  ?   --> My Logic 

Prime_List = []
Composite_List = []

def Appended_List():
   Limit = int(input("Set Your Limit :- "))
   i=0
   List = []
   while i<Limit:
        Number = int(input(f"Enter your {Limit}[{i}]  :-  "))
        List.append(Number)
        i+=1
   return List


def Check_Prime_Or_Composite(Number):
    if Number<=1:
        print(f"{Number} is neither a Prime or Composite")
        raise ValueError
    else:
        count=0
        j=1
        while(j<=Number):
            if Number%j==0:
                count+=1
            j+=1

        if count==2:
            return True
        else:
            return False
            

def Display():
    Prime_List = []
    Composite_List = []
    k=0
    numbers  = Appended_List()
    while k < len(numbers):
        if Check_Prime_Or_Composite(numbers[k]):
            Prime_List.append(numbers[k])
        else:
            Composite_List.append(numbers[k])
        k+=1
    return Prime_List , Composite_List

    
        
Prime_List , Composite_List  = Display()
print("Prime Numbers are :-   ",Prime_List)
print("Composite Numbers are :- ",Composite_List)


'''

Output :- 

Set Your Limit :- 5
Enter your 5[0]  :-  12
Enter your 5[1]  :-  3
Enter your 5[2]  :-  5
Enter your 5[3]  :-  7
Enter your 5[4]  :-  90
Prime Numbers are :-    [3, 5, 7]
Composite Numbers are :-  [12, 90]

'''