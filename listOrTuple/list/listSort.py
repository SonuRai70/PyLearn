numbers = [2, 7, 9, 2, 0, 5]
print(numbers.sort())   #sort change actual list
print("Sorted numbers are : ", numbers)
numbers.sort(reverse=True)
print(numbers)
numbers.reverse()
print(numbers)