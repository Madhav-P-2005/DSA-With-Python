# ⭐) Frequency Map / Dictionary 

# Store frequency in Dictionary 

d1 = {}

n = int(input("Enter the size of the store :-  "))

for i in range(n):

   num = int(input("Enter Number :- "))

   d1[num] = d1.get(num , 0) + 1

print("Frequency Map :- ", d1)


'''

Output :- 

Enter the size of the store :-  5
Enter Number :- 1
Enter Number :- 1
Enter Number :- 1
Enter Number :- 2
Enter Number :- 3
Frequency Map :-  {1: 3, 2: 1, 3: 1}

'''


# Anirudh Sir's  Method 1 :- 

nums = [5, 6 ,7 , 7 , 1 , 9 , 111 , 1, 1 , 5 ,1, 1]


freq_map = {}


for i in range(0, len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]] +=1
    else:
        freq_map[nums[i]] = 1


print("Frequency Map :- ",freq_map)


# Time Compexity  :-   T(n) = O(N)
# Space Complexity :-   S(n) = O(N)  


'''

Output :-  Frequency Map :-  {5: 2, 6: 1, 7: 2, 1: 5, 9: 1, 111: 1}

'''





# Anirudh Sir's  Method 2 (Pythonic Way)  :- 

nums = [5, 6 ,7 , 7 , 1 , 9 , 111 , 1, 1 , 5 ,1, 1]

hash_map = dict()

n = len(nums)

for i in range(0, n):
    hash_map[nums[i]] = hash_map.get(nums[i] , 0) + 1 


print("Frequency Map (Optimized Way) :- ",hash_map)



# Time Compexity  :-   T(n) = O(N)
# Space Complexity :-   S(n) = O(N)    



'''

Output :-   Frequency Map (Optimized Way) :-  {5: 2, 6: 1, 7: 2, 1: 5, 9: 1, 111: 1}

'''