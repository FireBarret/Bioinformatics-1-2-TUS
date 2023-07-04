# coding: Shift-JIS

array = [56,23,10,97,51,70,9,32,12,43]

max = array[0]
for n in range(0, len(array)):
    if array[n] > max:
        max = array[n]
    
min = array[0]
for n in range(0, len(array)):
    if array[n] < min:
        min = array[n]
avg = 0
for n in range(0, len(array)):
    avg += array[n] / len(array)
even = 0
for n in range(0, len(array)):
    if array[n] % 2 == 0:
        even += 1
odd = 0
for n in range(0, len(array)):
    if array[n] % 2 != 0:
        odd += 1            
print(max)
print(min)
print(avg)
print(even)
print(odd)
#����������ҏW���Ă��������B


