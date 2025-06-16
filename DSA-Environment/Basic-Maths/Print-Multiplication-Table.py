# Q11) Write a Program to Print Multiplication Table of any Number Using While Loop ?     --> My Logic
 
Number = int(input("Enter any Number :- "))
Limit = int(input("Set Your Limit :- "))
i = 1 

if Number<0:
          raise ValueError("Please enter a non-negative number")
else: 
    print(f"Multiplication Table of {Number} is :- ", "\n")
    while i<=Limit:
        result = Number  * i
        print(Number ,  "*" ,  i  , "=" , result)
        i+=1


'''

Output :- 

Enter any Number :- 5
Set Your Limit :- 10
Multiplication Table of 5 is :-  

5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50

'''



# Q11) Write a Program to Print Multiplication Table of any Number Using For -  Loop ?     --> My Logic 

Number = int(input("Enter any Value :- "))
Limit = int(input("Set your Limit :- "))
i = 1 

if Number<0:
      raise ValueError
else:
      print(f"Multiplication Table of {Number} is :- ")
      for i in range(1,  Limit+1): 
            result = Number * i
            print(Number , "*" ,  i , "=" , result)
            i+=1


'''

Output :- 

Enter any Value :- -34
Set your Limit :- 10
Traceback (most recent call last):
  File "e:\DSA with Python\DSA-Environment\Basic-Maths\Print-Multiplication-Table.py", line 45, in <module>
    raise ValueError
ValueError

'''




# Q11) Write a Program to Print Multiplication Table of any Number Using Do - While ?     --> My Logic 

Number = int(input("Enter any Number :- "))
Limit = int(input("Set Your Limit :- "))
i = 1

if Number<0:
        raise ValueError("Please enter a non-negative number")
else:
      print(f"Multiplication Table of {Number} upto {Limit} is :- \n")
      while i<=Limit:
            result = Number * i
            print(Number  , "*" , i  , "=" , result)
            i+=1



'''

Output :- 

Enter any Number :- -10
Set Your Limit :- 10
Traceback (most recent call last):
  File "e:\DSA with Python\DSA-Environment\Basic-Maths\Print-Multiplication-Table.py", line 77, in <module>
    raise ValueError("Please enter a non-negative number")
ValueError: Please enter a non-negative number

'''




# Q11) Write a Program to Print Multiplication Table of any Number Using Function ?     --> My Logic 

def  Multiply(Number):
      Limit = int(input("Set your Limit :- "))
      i=1
      if Number<0:
            raise ValueError("Please enter a non-negative number")
      else:
        print(f"Multiplication Table of {Number} upto {Limit} is :- \n")
        while(i<=Limit):
              result = Number * i
              print(Number , "*" , i , "=" , result)
              i+=1



Number = int(input("Enter any Number :- "))
Multiply(Number)



'''

Output :- 

Enter any Number :- 0
Set your Limit :- 10
Multiplication Table of 0 upto 10 is :- 

0 * 1 = 0
0 * 2 = 0
0 * 3 = 0
0 * 4 = 0
0 * 5 = 0
0 * 6 = 0
0 * 7 = 0
0 * 8 = 0
0 * 9 = 0
0 * 10 = 0

'''