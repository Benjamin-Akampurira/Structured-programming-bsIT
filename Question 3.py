n = int(input("Enter a positive number: "))
sum_even =0 

#Loop from 1 to n
for i in range(1, n + 1):
    if i % 2 ==0:
        sum_even += i

print("The sum of all even numbers numbers from 1 to",n,"is:", sum_even)
     
