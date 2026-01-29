# Recursion Using Parameters  


# Q3) Print x=15 using Recursion with Parameters n elements ? (Head)


# My Logic 
def Print(x , n):
    if n<=0:
        return
    n-=1
    print(x)
    Print(x , n)
    
Print(15 , 3)

'''

Output :- 

15
15
15

'''


# Sir's Logic
def Print(x , n):
    if n==0:
        return
    print(x)
    Print(x , n-1)
    
Print(15 , 3)


'''

Output :- 

15
15
15

'''



# Q4) Print 1 to N elements using  Head Recursion ? 

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



# Q5) Print N to 1 elements using Tail Recursion (Backtracking) ? 


def func_back(i, size):
     
     if i>size:
          return
     func_back(i+1 , size)
     print(i)

func_back(1,5)


'''

Output :- 

5
4
3
2
1

'''