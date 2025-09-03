# Q1) Print Anirudh 4 times using Recursion  (Head Recursion) ?

# Note :- You first do the job then call the function it is called Head Recursion 

# count=0
# def Name():
#     global count    # tell Python you’re modifying the global variable
#     if count==4:
#         return
#     print("Anirudh")
#     count+=1
#     Name()

# Name()


'''

Output :- 

Anirudh
Anirudh
Anirudh
Anirudh

'''



# Q2) Print Anirudh 4 times using Recursion  (Tail Recursion or Backtracking) ?

# Note :-  You first call the function then do the job is called Tail Recursion.

# count=0
# def Name():
#     global count
#     if count==4:
#         return
#     count+=1
#     Name()
#     print("Anirudh")

# Name()


'''

Output :- 

Anirudh
Anirudh
Anirudh
Anirudh

'''




# Q3) Print x=15 using Recursion with Parameters n elements ? 


# My Logic 
# def Print(x , n):
#     if n<=0:
#         return
#     n-=1
#     print(x)
#     Print(x , n)
    
# Print(15 , 3)

'''

Output :- 

15
15
15

'''


# Sir's Logic
# def Print(x , n):
#     if n==0:
#         return
#     print(x)
#     Print(x , n-1)
    
# Print(15 , 3)


'''

Output :- 

15
15
15

'''



# Q4) Print 1 to N elements using Recursion ? 

# My Logic 
def Print(i , size):
      if i==size:
          return
      i+=1
      print(i)
      Print(i, size)
    

Print(0 , 5)

'''

Output :- 

1
2
3
4
5

'''



# Anirudh Sir's Logic :- 

def func(i, n):
     if i>n:
          return
     print(i)
     func(i+1, n)

func(1, 5)


'''

Output :- 

1
2
3
4
5

'''