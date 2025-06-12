# 10) To Print all the Factors of a given Number Using While Loop  (Example :-  12 => 1 , 2 , 4 , 6 , 8, 12)  --> My Logic 

Number = int(input("Enter any Number :- "))
print(f"All factors of {Number} are :- ")
i = 1 

while i<=Number:
        if Number%i==0:
                print(i)
        i+=1


'''

Output :- 

Enter any Number :- 5
All factors of 5 are :- 
1
5

'''



# 10) To Print all the Factors of a given Number Using For - Loop    --> My Logic 

Number  = int(input("Enter any Number :-  "))
print(f"All factors of {Number} are :- ")
i = 1 

for i in range(1, Number+1):
        if Number%i==0:
             print(i)


'''

Output :-

Enter any Number :-  12
All factors of 12 are :- 
1
2
3
4
6
12

'''



# 10) To Print all the Factors of a given Number Using While - Loop      -->   My Logic 

Number  = int(input("Enter any Number :-  "))

if Number==0:
      print("0 has no factors")
else:
     print(f"All factors of {Number} are :- ")
     i=1
     while i<=Number:
               if Number%i==0:
                   print(i)
               i+=1


'''

Output :- 

Enter any Number :-  0
0 has no factors

'''



# 10) To Print all the Factors of a given Number Using Functions      -->   My Logic 

def All_Factors(Number):
       lst = []
       i=1
       while i<=Number:
             if Number%i==0:
               lst.append(i)   
             i+=1
       return lst

Number = int(input("Enter any Number :- "))
print(f"All Factors of {Number} are :- ",All_Factors(Number))



'''

Output :- 

Enter any Number :- 8
All Factors of 8 are :-  [1, 2, 4, 8]


'''