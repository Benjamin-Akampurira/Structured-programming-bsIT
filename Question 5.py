numbers =[]
#Allow the user to input the numbers
print("Enter five numbers")
for i in range(5):
    num =int(input())
    numbers.append(num)

#call for instructions
print("numbers:", numbers)
print("Maximum:", max(numbers))
average =sum(numbers)/len(numbers)
print("Average:", average)
print("Sorted:", sorted(numbers))
   