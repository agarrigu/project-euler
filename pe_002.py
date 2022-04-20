# Find the sum of even Fibonacci numbers below 4 000 000
# These are more fun to figure out by yourself!

''' Four million is pretty big, let's not make this recursive :(
'''
# TODO Find a better way, I feel like I'm using too many variables
def main():
    sum = 2
    f1 = 2
    f0 = 1
    n = 0
    while n < 4_000_000:
        n = f0 + f1
        f0 = f1
        f1 = n
        if n % 2 == 0:
            sum += n

    print(sum)

if __name__ == '__main__':
    main()
