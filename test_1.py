from typing import List

# All available tokens
OPEN_BRACKET = "("
CLOSING_BRACKET = ")"

lexemes = [
    OPEN_BRACKET,
    CLOSING_BRACKET,
]


def parse(string: str) -> List[str]:
    """The function that parses a string into tokens list"""
    return list(string)


def lexical_check(sequence: List[str]):
    """The function that checks is all tokens are known"""
    for i in sequence:
        if i not in lexemes:
            return False
    return True


def syntax_check(sequence: List[str]) -> bool:
    """
    The function that checks syntax.
    Algorithm:
        1) Initialize cursor;
        2) Check if the first token by a cursor equals an open bracket. If it is not, we have invalid input;
        3) Initialize a counter to 0;
        4)  While the cursor less than sequence length:  if we have a '(', increment the counter if we have a ')',
        decrement the counter, increment the cursor, if the counter reaches 0 - break;
        5) Check if the counter is not 0, we have an invalid sequence (unbalanced brackets);
        6) if the cursor less than sequence length, return to step 2;
    """

    def on_open_bracket(c):
        """A handler that will be triggered when an open bracket token founded"""
        return c + 1

    def on_closing_bracket(c):
        """A handler that will be triggered when a closing bracket token founded"""
        return c - 1

    def on_unknown_character(c):
        """A handler that will be triggered when an unknown token founded"""
        raise ValueError('Unknown character!')

    # A dictionary that stores all token handlers
    actions: dict = dict.fromkeys(lexemes)
    actions[OPEN_BRACKET], actions[CLOSING_BRACKET] = on_open_bracket, on_closing_bracket

    cursor = 0
    while len(sequence) > cursor:
        # Check if the first token by a cursor equals an open bracket
        if sequence[cursor] != OPEN_BRACKET:
            return False

        counter = 0

        while cursor < len(sequence):
            # Increase or decrease the counter depending on which token we have.
            func = actions.get(sequence[cursor], on_unknown_character)
            counter = func(counter)
            cursor += 1
            if counter == 0:
                break

        if counter != 0:
            return False

    return True


def is_correct(sequence: List[str]) -> bool:
    # Lexical check
    is_lexical_correct = lexical_check(sequence)
    # If lexical check passed, syntax check
    if is_lexical_correct:
        return syntax_check(sequence)

    return is_lexical_correct


def quick_test():
    test_strings = [
        "()",
        ")(",
        "))",
        "((",
        "()(",
        "())(",
        "()()",
        "(())",
        "(()())",
        "(()(()))",
    ]

    for test_case in test_strings:
        test_sequence = parse(test_case)
        print(f"{test_case}: {is_correct(test_sequence)}")


if __name__ == '__main__':
    print("Test: ")
    quick_test()

    print()
    test_string = input("Test string: ")
    test_sequence = parse(test_string)
    print("Is correct string? ", is_correct(test_sequence))
