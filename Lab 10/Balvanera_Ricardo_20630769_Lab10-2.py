# Initialize a loop to prevent negative input
k = -1
while k < 0:
    # Input statement
    k = int(input("Please input k: "))
    if k < 0:
        print("Please input a positive number")
    else:
        break

# Print the first K prime numbers
count = 0
number = 2
while count < k:
    is_prime = True
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                is_prime = False
                break
        if is_prime:
            print(number, end=" ")
            count += 1
    number += 1
