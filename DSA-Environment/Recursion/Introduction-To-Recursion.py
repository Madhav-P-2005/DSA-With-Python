# Q1) Print Anirudh 4 times using Recursion  (Head Recursion) ?

# Note :- You first do the job then call the function it is called Head Recursion 

count=0
def Name():
    global count    # tell Python you’re modifying the global variable
    if count==4:
        return
    print("Anirudh")
    count+=1
    Name()

Name()


'''

Output :- 

Anirudh
Anirudh
Anirudh
Anirudh

'''



# Q2) Print Anirudh 4 times using Recursion  (Tail Recursion or Backtracking) ?

# Note :-  You first call the function then do the job is called Tail Recursion.

count=0
def Name():
    global count
    if count==4:
        return
    count+=1
    Name()
    print("Anirudh")

Name()


'''

Output :- 

Anirudh
Anirudh
Anirudh
Anirudh

'''