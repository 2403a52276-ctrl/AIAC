from typing import Any, List

#!/usr/bin/env python3
"""
task1.py

Implement a simple Stack using a Python list with push, pop, peek, and is_empty.
Includes docstrings, comments, and basic test cases.
"""



class Stack:
    """Simple LIFO stack implemented with a Python list."""

    def __init__(self) -> None:
        """Create an empty stack."""
        self._items: List[Any] = []

    def push(self, item: Any) -> None:
        """
        Push an item onto the top of the stack.

        Args:
            item: Any Python object to store on the stack.
        """
        # Append to the end of the list -> top of stack
        self._items.append(item)

    def pop(self) -> Any:
        """
        Remove and return the top item from the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> Any:
        """
        Return the top item without removing it.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        """
        Return True if the stack is empty, False otherwise.

        This is the one-shot-added method that checks emptiness.
        """
        return len(self._items) == 0

    def __len__(self) -> int:
        """Return number of items in the stack."""
        return len(self._items)

    def __repr__(self) -> str:
        """Return a debug representation of the stack."""
        return f"Stack({self._items})"


# Basic test cases
def _run_tests() -> None:
    s = Stack()
    # New stack should be empty
    assert s.is_empty() is True
    try:
        s.peek()
        assert False, "peek on empty should raise"
    except IndexError:
        pass
    try:
        s.pop()
        assert False, "pop on empty should raise"
    except IndexError:
        pass

    # Push items and check LIFO behavior
    s.push("first")
    s.push("second")
    s.push("third")
    assert s.is_empty() is False
    assert len(s) == 3
    assert s.peek() == "third"  # top should be last pushed
    assert s.pop() == "third"
    assert s.pop() == "second"
    assert s.pop() == "first"
    assert s.is_empty() is True

    # Mixed types
    s.push(1)
    s.push(None)
    s.push([3, 4])
    assert s.peek() == [3, 4]
    assert s.pop() == [3, 4]
    assert s.pop() is None
    assert s.pop() == 1

    print("All tests passed.")


if __name__ == "__main__":
    _run_tests()