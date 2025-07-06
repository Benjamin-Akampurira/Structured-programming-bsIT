def is_prime(n):
    if n <= 1:  #I HAVE A QUESTION HERE
        return False
    for i in range(2, int(n**0.5)+1): #I HAVE A QUESTION HERE
        if n % i == 0: 
            return False
    return True

#Ask user to insert number
num = int(input("Enter a number:"))

#Call the function and print result
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
