# Q2) Character Hashing in Specific Way ? 

s = "azyxyyzaaaa"

q = ["d" , "a" , "y", "x"] 

hash_list = [0] * 26        

print("hash_list :- ",hash_list)   # Output :-   hash_list :-  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for ch in s:

    ascii_value = ord(ch)

    index = ascii_value - 97

    hash_list[index] +=1


Hash_List = []

print("Hash List of q :- ")
for ch in q:
    
    ascii_value = ord(ch)

    index = ascii_value - 97

    Hash_List.append(hash_list[index])
print(Hash_List)



# Time Complexity :-   O(s + q)    
# Space Complexity :-  O(1)     


'''

Output :- 

Hash List of q :-
[0, 5, 3, 1]

'''



# Q2) Character Hashing in General Way ? 

s = "aaz*&cWXY!%BMM$@@&&"

q = ["*" , "A" , "B" , "&" , "M" , "%", "a" , "@" , "!", "c"]

hash_list2 = [0] * 127

empty_list = []

print("Hash List 2 :- ",hash_list2)       # Output :- Hash List 2 :-  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


for ch in s:

    ascii_value = ord(ch)

    index = ascii_value - 32

    hash_list2[index]+=1


for ch in q:

    ascii_value = ord(ch)

    index = ascii_value - 32

    empty_list.append(hash_list2[index])
print("Hash List 2 :- ",empty_list)          # Output :-   Hash List 2 :-  [1, 0, 1, 3, 2, 1, 2, 2, 1, 1]


# Time Complexity :-  O(s + q)    
# Space Complexity :-  O(1)     