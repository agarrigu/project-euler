# Find the largest palindrome made from the product of two 3-digit numbers.
# These are more fun if you figure them out yourself!
'''
This is a better method but still could be better.
TODO: find out properties of palindrome numbers, make BETTER!
'''

def main():
    largest_palindrome = 0
    for i in range(999, 99, -1):
        for j in range(999, i, -1):
            candidate = i * j
            if candidate < largest_palindrome:
                break
            if is_palindrome(candidate) and candidate > largest_palindrome:
                largest_palindrome = candidate
    print(largest_palindrome) 


def is_palindrome(n: int) -> bool:
    s = str(n)
    for i in range(len(s) // 2):
        if not s[i] == s[-(i + 1)]:
            return False
    return True

if __name__ == '__main__':
    main()
