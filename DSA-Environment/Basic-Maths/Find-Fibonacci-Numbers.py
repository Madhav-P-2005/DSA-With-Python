# Q16) Find the  Fibonacci Numbers using while Loop (Example :-   0,1,1,2,3,5,8.......) ?   --> My Logic 

# Number1 = 0
# Number2 = 1 
# Number3 = 0
# Limit = int(input("Set Your Limit :- "))

# print(f"The Fibonacci Numbers are :- ")
# print(Number1)
# while(Number3<Limit):
#     Number1 = Number2
#     Number2 = Number3
#     Number3 = Number1 + Number2
#     if Number3>Limit:
#         break
#     print(Number3)



'''

Output :-

Set Your Limit :- 8
The Fibonacci Numbers are :- 
0
1
1
2
3
5
8

'''



# Q16) Find the  Fibonacci Numbers using For - Loop  ?   --> My Logic 

# Number1 = 0 
# Number2 = 1 
# Number3 = 0 
# Limit = int(input("Set Your Limit :- "))
# i=0

# print("The Fibonacci Numbers are :-  ")
# print(Number1)
# for i in range(1, Limit):
#     Number1 = Number2
#     Number2 = Number3
#     Number3 = Number1 + Number2
#     if Number3>Limit:
#         break
#     print(Number3)



'''

Output :- 

Set Your Limit :- 21
The Fibonacci Numbers are :-  
0
1
1
2
3
5
8
13
21

'''



# Q16) Find the  Fibonacci Numbers using Do - While Loop  ?   --> My Logic 

# Number1 = 0
# Number2 = 1
# Number3 = 0
# Limit = int(input("Set Your Limit :- "))

# print("The Fibonacci Numbers are :-  ")
# print(Number1)

# if Limit<=0:
#     print(f"Invalid Limit :- {Limit}")
# else:
#   while True:
#     if Number3!=Limit:
#         Number1 = Number2
#         Number2 = Number3
#         Number3 = Number1 + Number3
#         if Number3>Limit:
#             break
#         print(Number3)
#     else:
#         break



'''

Output :- 

Set Your Limit :- 35
The Fibonacci Numbers are :-  
0
1
1
2
3
5
8
13
21
34

'''



# Q16) Find the  Fibonacci Numbers using Functions  ?   --> My Logic 

def Print_Fibonacci():
      Fibonacci_Numbers = [0, 1]
      Limit = int(input("Set Your Limit :- "))
      if Limit<=0:
          print(f"Invalid Limit :- {Limit}")
      else:
          print("The Fibonacci Numbers are :-  ")
          while True:
               sum_of_2 = sum(Fibonacci_Numbers[-2:])
               if sum_of_2>Limit:
                        break
               Fibonacci_Numbers.append(sum_of_2)
          return Fibonacci_Numbers
       

print(Print_Fibonacci())


'''

Output :- 

Set Your Limit :- 20
The Fibonacci Numbers are :-  
[0, 1, 1, 2, 3, 5, 8, 13]

'''