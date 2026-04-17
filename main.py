firstNumber = int(input("Enter starting value: "))
lastNumber = int(input("Enter ending value: "))


def find_perfect_numbers(firstNumber, lastNumber):
    perfect_numbers = [n for n in range(firstNumber, lastNumber + 1) if perfectPrime(n)]
    if perfect_numbers:
        print(", ".join(map(str, perfect_numbers)))

def determineDivisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors

def perfectPrime(n):
    return sum(determineDivisors(n)) == n

find_perfect_numbers(firstNumber, lastNumber)