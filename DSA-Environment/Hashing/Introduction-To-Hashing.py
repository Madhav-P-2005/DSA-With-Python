# Q1) Count how many times the no of m[i] values come in n ? 

n = [5 ,3 ,2 ,2 , 1 , 5 , 5, 7 ,5 , 10]

m = [10 , 111 , 1 , 9 , 5 , 67 , 2]

count = 0

m_count=[]

freq_map = {}

for i in range(0, len(n)):
    if n[i] in freq_map:
        freq_map[n[i]]+=1
    else:
        freq_map[n[i]] = 1
print("Frequency Map :- ", freq_map)        # Output :-  Frequency Map :-  {5: 4, 3: 1, 2: 2, 1: 1, 7: 1, 10: 1}


for i in range(0, len(m)):
    if m[i] in freq_map:
        m_count.append(freq_map[m[i]])
    else:
        m_count.append(0)
print("m_count :- ", m_count)              # Output :-   m_count :-   [1, 0, 1, 0, 4, 0, 2]



# Without m_count ? :- 
# total = 0
# for i in range(0, len(m)):
#     if m[i] in freq_map:
#         total+= freq_map[m[i]]
# print("Total :- ",total)     # Output :-   Total :-  8
    




# Anirudh Sir's Solution (Brute Force) :- 

for i in m:
    count=0
    for j in n:
        if j==i:
            count+=1
    print(count)


'''

Output :- 

1
0
1
0
4
0
2

'''