# Q17) Find the Tribonacci Numbers Using While Loop  ? (Example :-  0 , 1 , 1 , 2 , 4 , 7 , 13)   --> My Logic 

Number1 = 0
Number2 = 1 
Number3 = 1
Number4 = 0
Limit = int(input("Set Your Limit :- "))
if Limit<=0:
  print(f"Error :- Invalid Limit :- {Limit}")
else:
  print("The Tribonacci Numbers are :-  ")
  print(Number1)
  print(Number2)
  print(Number3) 
  while Number4<Limit-1:
      Number4 = Number1 + Number2 + Number3
      if Number4>Limit:
           break
      print(Number4)
      Number1 = Number2
      Number2 = Number3
      Number3 = Number4


'''

Output :- 

Set Your Limit :- 13
The Tribonacci Numbers are :-  
0
1
1
2
4
7
13

'''


# Q17) Find the Tribonacci Numbers Using For - Loop  ?     --> My Logic 

Number1 = 0
Number2 = 1 
Number3 = 1
Number4 = 0
Limit = int(input("Set Your Limit :- "))
if Limit<=0:
   print(f"Error :- Invalid Limit :- {Limit}")
else:
  print("The Tribonacci Numbers are :-  ")
  print(Number1)
  print(Number2)
  print(Number3)
  for i in range(1 , Limit):
      Number4 = Number1 + Number2 + Number3
      if Number4>Limit:
          break
      print(Number4)
      Number1 = Number2
      Number2 = Number3
      Number3 = Number4


'''

Output :- 

Set Your Limit :- 7
The Tribonacci Numbers are :-  
0
1
1
2
4
7

'''



# Q17) Find the Tribonacci Numbers Using Do - While Loop ?    --> My Logic 

Number1 = 0
Number2 = 1 
Number3 = 1
Number4 = 0
Limit = int(input("Set Your Limit :- "))
if Limit<=0:
  print(f"Error :- Invalid Limit :- {Limit}")
else:
  print("The Tribonacci Numbers are :-  ")
  print(Number1)
  print(Number2)
  print(Number3)
  while True:
    if Number4<Limit:
        Number4 = Number1 + Number2 + Number3
        if Number4>Limit:
            break
        print(Number4)
        Number1 = Number2
        Number2 = Number3
        Number3 = Number4
    else:
        break


'''

Output :- 

Set Your Limit :- -5
Error :- Invalid Limit :- -5

'''



# Q17) Find the Tribonacci Numbers Using Function with Lists  ?   --> My Logic 


def Tribonacci_Numbers():
     Limit = int(input("Set your Limit :- "))
     if Limit<=0:
           print(f"Error :- Invalid Limit :- {Limit}")
     else:
           Tribonacci_Series = [0,1,1]
           print("The Tribonacci Numbers are :-  ")
           while True:
                 Sum_of_last_3 = sum(Tribonacci_Series[-3:])   
                 if Sum_of_last_3>Limit:
                           break
                 Tribonacci_Series.append(Sum_of_last_3)
           return Tribonacci_Series
   

print(Tribonacci_Numbers())


'''

Output :- 

Set your Limit :- 30
The Tribonacci Numbers are :-  
[0, 1, 1, 2, 4, 7, 13, 24]

'''