"""
Find if num is palindrome
"""


def is_palindrome(n: int) -> bool:

    # Negative numbers always False due to - sign
    if n < 0:
        return False

    new_n = int(str(n)[::-1])

    return n == new_n


if __name__ == '__main__':

    test = is_palindrome(1213)
    print(test)
