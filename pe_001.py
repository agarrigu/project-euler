# Find the sum of all the multiples of 3 or 5 below 1000
# These are more fun to figure out on your own!

def main():
    answer = sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])
    print(answer)

if __name__ == '__main__':
    main()
