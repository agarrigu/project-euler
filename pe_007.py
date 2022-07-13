# What is the 10 001st prime number?
# These are more fun to figure out on your own!
import math

def main():
    print_last_factor()

# Let's be efficient: after 3 all prime numbers are either 6n+1 or 6n-1. We 
# are keeping the factors in a list, instead of just keeping the last found, 
# sincek I'm pretty sure its more efficient to keep this list and check new 
# candidates against old primes, since all numbers have at least one prime as 
# a factor.

def print_last_factor():
    factors = [2, 3]
    i = 1
    while len(factors) < 10_001:
        six_n = i * 6
        s_n_m = six_n - 1
        s_n_p = six_n + 1
        if is_prime(s_n_m, factors):
            factors.append(s_n_m)
            print(s_n_m)
        if is_prime(s_n_p, factors):
            factors.append(s_n_p)
            print(s_n_p)
        i += 1

    print(factors[-1])

# Here we are checking the candidate against ALL primes found thus far, where 
# we should only be checking until we reach the largest possible factor
# TODO: make the commented out code work.

def is_prime(candidate, factors):
    i = 0
    # max_poss = candidate / 2
    # while factors[i] < max_poss and i < len(factors):
    while i < len(factors):
        if candidate % factors[i] == 0:
            return False
        # max_poss = math.floor(candidate / factors[-1])
        i += 1

    return True

if __name__ == "__main__":
    main()
