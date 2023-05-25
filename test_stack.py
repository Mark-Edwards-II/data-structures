from stack import Stack
def test_stack():
    """
    Test each method in stack class
    """
    stack=Stack()
    assert stack.is_empty() == True
    stack.push("a")
    stack.push("b")
    assert stack.size() == 2
    # stack.display should print `b -> a`
    stack.display()
    assert stack.top() == "b"
    assert stack.pop() == "b"
    assert stack.size() == 1
    # stack.display() should print `a`
    stack.display()
    assert stack.pop() == "a"
    assert stack.is_empty() == True

    


if __name__ == "__main__":
    test_stack()