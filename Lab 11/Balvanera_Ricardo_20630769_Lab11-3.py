#define the function header
def is_prime(n):
#base case 
    if n <= 1:
        return False
#if n > 1 loop and find if # is prime
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
#input statement
user_input = int(input("Please input an integer: "))
#call the function header and print results
if is_prime(user_input):
    print(user_input, "is a prime number.")
else:
    print(user_input, "is not a prime number.")
