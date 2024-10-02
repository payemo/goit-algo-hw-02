from collections import deque

def is_palindrome(s: str) -> bool:
    """
    Determine whether the given string is a palindrome.
    
    This function ignores case and spaces, and uses a deque to compare
    characters from both ends of the string efficiently.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string palindrome, False otherwise. 
    """

    # remove spaces and convert to lowercase
    cleaned_str = ''.join(ch.lower() for ch in s if not ch.isspace())

    char_deq = deque(cleaned_str)

    while len(char_deq) > 1:
        front_ch = char_deq.popleft()
        back_ch = char_deq.pop()
        if front_ch != back_ch:
            return False
    
    return True

def main():
    test_cases = [
        "А роза упала на лапу Азора",
        "Hello World",
        "Madam",
        "Step on no pets",
        "12321",
        "12345"
    ]

    for test in test_cases:
        result = is_palindrome(test)
        print(f"'{test}' -> {result}")

if __name__ == '__main__':
    main()