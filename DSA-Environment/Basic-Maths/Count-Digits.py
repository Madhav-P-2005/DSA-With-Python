# 1) Count Digits Using while - Loop ?   ---> My Logic

Number = int(input("Enter any value :-  "))
temp = abs(Number)    # abs() :- Copies only the magnitude (i.e., makes it positive)
count = 0

if temp==0:
      count+=1
else: 
    while temp>0:
        temp = temp//10
        count+=1


print(f"Total digits in {Number} is :- ",count)



# 2) Count Digits Using for - loop ?   ---> My Logic   (Note :- # ⚠️ Using for is not natural here..)

Number = int(input("Enter any value :-  "))
temp = abs(Number)   
count = 0


for i in range(temp):
    if(temp>0):
        temp = temp//10
        count+=1


print(f"Total digits in  {Number} is :- ",count)



# 2) Count Digits  Using  do - While  loop ?   ---> My Logic

Number = int(input("Enter any value :-  "))
temp = abs(Number)   
count = 0


while True:
    count+=1
    temp = temp//10
    if temp==0:
        break


print(f"Total digits in  {Number} is :- ",count)



# 2) Count Digits  Using  Function ?   ---> My Logic

def CountNum(Number):
    temp = abs(Number)
    count = 0

    if temp == 0:
        return 1 
    
    while temp>0:
        temp = temp//10
        count+=1
        
    return count


Number = int(input("Enter any Value :- "))
Ans  = CountNum(Number)
print(f"Total digits in {Number} is :- ",Ans)