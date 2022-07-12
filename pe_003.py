# What is the largest prime factor of the number 600,851,475,143?
# These are more fun if you figure them out yourself!
# Fixes, improvements: Start checking backwards!! argv int validator ??
import sys

def largest_prime_factor(n: int) -> int:
    # MAX_FACT = n // 3 # There is a more precise number but its a float
    primes = [2, 3] # Populate primes that don't follow 6n±1 rule
    prime_factors = []
    

    for i in range(1, n // 6 + 1): #MAX_FACT // 6):
        six_n_minus_one = i * 6 - 1
        six_n_plus_one = i * 6 + 1
        print(six_n_minus_one)
        print(six_n_plus_one)
        print(prime_factors)
        if all(six_n_minus_one % prime != 0 for prime in primes):
            primes.append(six_n_minus_one)
            if n % six_n_minus_one == 0:
                prime_factors.append(six_n_minus_one)
        if all(six_n_plus_one % prime != 0 for prime in primes):
            primes.append(six_n_plus_one)
            if n % six_n_plus_one == 0:
                prime_factors.append(six_n_plus_one)

    return prime_factors[-1]

def main():
    if len(sys.argv) == 1:
        print(largest_prime_factor(10))
    print(largest_prime_factor(int(sys.argv[1])))

if __name__ == '__main__':
    main()
