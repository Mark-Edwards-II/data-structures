from stack import Stack
# A list would be much more simple.

def is_balanced(brackets: str):
    """
    Singly linked Stack implementation of checking for balanced brackets in a string. 
    """
    stacked_brackets = Stack()
    for char in brackets:
        if char in "({[":
            stacked_brackets.push(char)
        else:
            if not stacked_brackets.is_empty() and (
                (stacked_brackets.top() == '(' and char == ')') or
                (stacked_brackets.top() == '{' and char == '}') or
                (stacked_brackets.top() == '[' and char == ']')
                ):
                # when ever we find a balanced couple remove the top item in the stack since only opening brackets are added.
                stacked_brackets.pop()
            else:
                return False
    # Stack should be empty when given a balanced string of brackets by this point.
    return stacked_brackets.is_empty()


if __name__ == "__main__":
    assert is_balanced("{") == False
    assert is_balanced("{[()]}") == True
    assert is_balanced("{{}}]") == False
    assert is_balanced("[{}()]") == True
    assert is_balanced("]{}") == False
