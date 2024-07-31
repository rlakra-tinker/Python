#
# Author: Rohtash Lakra
#

# Python 3: Fibonacci series up to n
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b

    print()


# Print Fibonacci Series of N numbers
# fib(1000)


def is_prime(n):
    if n <= 1:
        return False

    if n > 1:
        for num in range(2, n):
            if (n % num) == 0:
                return False

    return True


# Print N prime numbers
def prime(n):
    for num in range(1, n):
        # print(num)
        if is_prime(num):
            print(num)


# prime(5)


# Print N prime numbers
def primes(n):
    ctr = 0
    while ctr < n:
        for num in range(1, n * n):
            if ctr == n:
                break

            if is_prime(num):
                print(num)
                ctr += 1


# primes(10)

# Print N prime numbers
def get_primes(n):
    primes = []
    while len(primes) < n:
        for num in range(1, n * n):
            if len(primes) == n:
                break

            if is_prime(num):
                primes.append(num)

    return primes


# print(get_primes(5))

from string import ascii_lowercase


def get_primes_mapping_with_ascii_lowercase():
    alpha_primes = {}
    primes = get_primes(26)

    index = 0
    for letter in ascii_lowercase:
        # print(f"index:{index}, letter:{letter}")
        alpha_primes[letter] = primes[index]
        index += 1

    return alpha_primes


# print(get_primes_mapping_with_ascii_lowercase())

def is_anagram(left, right):
    alpha_primes = get_primes_mapping_with_ascii_lowercase()

    left_result = 1
    for letter in left.lower():
        if letter.isalpha():
            left_result *= alpha_primes[letter]

    # print(left_result)

    right_result = 1
    for letter in right.lower():
        if letter.isalpha():
            right_result *= alpha_primes[letter]

    # print(right_result)

    return left_result == right_result


# print(is_anagram("left", "f9?Le1T"))

print()
fruits = ["apple", "banana", "orange"]
print(fruits)
print(list(enumerate(fruits)))
print(hash(enumerate(fruits)))
print(id(enumerate(fruits)))

print()
loud_fruits = [fruit.upper() for fruit in fruits]
print(loud_fruits)

print()
print(list(enumerate(loud_fruits)))
print(hash(enumerate(loud_fruits)))
print(id(enumerate(loud_fruits)))
print("\n")

print()
input = 97
print(f"input:{input}, str:{str(input)}, ascii:{ascii(input)}, oct:{oct(input)}")
print(f"hex:{hex(input)}, bin:{bin(input)}, chr:{chr(input)}")
print()

print("\n")
for index in range(1, 10, 2):
    print(index)
print()
