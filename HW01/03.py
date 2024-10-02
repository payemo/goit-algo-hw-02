from typing import List

def check_delimiters(s: str) -> str:
    """
    Defines whether the sequence of characters is symmetrical in a row.

    Function ignores all symbols except delimiters: (), [], {}.
    
    Args:
        s (str): Input string for checking.

    Returns:
        str: "Symmetrical" if delimiters are balanced, "Non-symmetrical" otherwise.
    """

    matching_delims = {
        '(' : ')',
        '[' : ']',
        '{' : '}'
    }

    opening_delims = set(matching_delims.keys())
    closing_delims = set(matching_delims.values())

    stack: List[str] = []

    for ch in s:
        if ch in opening_delims:
            stack.append(ch)
        elif ch in closing_delims:
            if not stack:
                return "Несиметрично"
            last_open = stack.pop()
            if matching_delims[last_open] != ch:
                return "Несиметрично"
            
    if not stack:
        return "Симетрично"
    else:
        return "Несиметрично"
    

def extract_delims(s: str) -> str:
    """
    Retrieves only delimiters symbols from input string.

    Args:
        s (str): Input string.
    
    Returns:
        str: Row with retrieved delimiters.
    """

    delims = {'(', ')', '[', ']', '{', '}'}
    return ''.join(ch for ch in s if ch in delims)

def main():
    test_cases = [
        "( ){[ 1 ]( 1 + 3 )( ){ }}}",
        "( 23 ( 2 - 3);",
        "( 11 }",
        "",
        "((()))", 
        "([{}])",
        "([{])",
        "{[()()]}",
        "{[(])}",                     
        "(((((((((())))))))))",       
        "((((((((((",                 
        "}}}}",                       
    ]

    for test in test_cases:
        delims_only = extract_delims(test)
        result = check_delimiters(delims_only)
        print(f"'{test}' -> {result}")
     

if __name__ == '__main__':
    main()