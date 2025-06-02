# 1)  Extraction of Digits using Loops !   ---> My Logic 

Number = int(input("Enter your Number :- "))
while(Number>0):
    remainder = Number%10
    print(remainder)
    Number = Number//10


'''

Output :- 

3
7
8
5

'''



# 1)  Extraction of Digits using for-loop !   ---> My Logic

Number = int(input("Enter your Number (using for Loop ) :- "))

for i in range(Number):
    if(Number>0):
        remainder = Number%10
        print(remainder)
        Number = Number//10


'''

Output :- 

Enter your Number (using for Loop ) :- 1234
4
3
2
1

'''



# 1) Extraction of Digits using Do-while ?   ---> My Logic

Number = int(input("Enter your Number (using Do - While) :- "))
 
while True:
   if(Number>0):
    remainder = Number%10
    print(remainder)
    Number = Number//10
   else:
     break
   

'''

Enter your Number (using Do - While) :- 1234
4
3
2
1

'''
   


# 1) Extraction of Digits using Function() ?    ---> My Logic

def Extract(Number):
  while(Number>0):
    remainder = Number%10
    print(remainder)
    Number = Number//10
  


Number = int(input("Enter your Number (using Function ) :- "))
Extract(Number)