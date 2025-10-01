## hashing :- 
## 01 count the frequency
def freq(arr,n):
    count = 0
    for i in arr:
        if i == n:
            count +=1
    return count
            
print(freq([1,1,5,1,6],1))


# 02 check the list and add it to dictonary with their frequency:-
arr = [1,2,3,4,1,5,6,0]

n = len(arr)
freq_map = dict()

for i in range (n):
    if arr[i] in freq_map:
        freq_map[arr[i]] +=1
    else :
        freq_map[arr[i]] =1
print(freq_map)

# 03 frequency in limited array :-
arr= [2, 3, 2, 3, 5]
freq_map = dict()
n = len(arr)
for i in range(n):
    freq_map[arr[i]] = freq_map.get(arr[i],0) + 1

full_freq = dict()
for j in range(6):
    full_freq[j] = freq_map.get(j, 0)

array = list(full_freq.values())   
print(array)

    
    

