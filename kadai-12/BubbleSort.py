array = [23,15,64,23,42,12,92]

def asc_bubble_sort(aList):
	sorted_list = aList[:]

	for i in range(0, len(sorted_list)):
		for j in range(1, len(sorted_list) - i):
			if sorted_list[j - 1] > sorted_list[j]:
				sorted_list[j], sorted_list[j - 1] = sorted_list[j - 1: j + 1]
				#print(sorted_list) #debug
				
	return sorted_list
def desc_bubble_sort(aList):
	sorted_list = aList[:]

	for i in range(0, len(sorted_list)):
		for j in range(1, len(sorted_list) - i):
			if sorted_list[j - 1] < sorted_list[j]:
				sorted_list[j], sorted_list[j - 1] = sorted_list[j - 1: j + 1]
				#print(sorted_list) #debug
				
	return sorted_list
print(asc_bubble_sort(array))
print(desc_bubble_sort(array))