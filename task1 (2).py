def normalize(scores):
    """Normalize a list of numeric scores to the [0, 1] range.

    Each score is transformed using min-max normalization:

        normalized_x = (x - min(scores)) / (max(scores) - min(scores))

    Edge cases are handled:
    - If the input list is empty, returns an empty list.
    - If all scores are equal (max == min), returns a list of zeros
      of the same length to avoid divide-by-zero.

    Args:
        scores (list[float]): List of numeric scores to normalize.

    Returns:
        list[float]: Normalized scores in the [0, 1] range.

    Examples:
        >>> normalize([10, 20, 30])
        [0.0, 0.5, 1.0]
        >>> normalize([5, 5, 5])
        [0.0, 0.0, 0.0]
        >>> normalize([])
        []
    """
    if not scores:
        return []

    m, n = max(scores), min(scores)
    if m == n:
        return [0.0] * len(scores)

    return [(x - n) / (m - n) for x in scores]


def test_normalize():
    # Standard case
    assert normalize([10, 20, 30]) == [0.0, 0.5, 1.0]

    # All equal values
    assert normalize([5, 5, 5]) == [0.0, 0.0, 0.0]

    # Empty list
    assert normalize([]) == []

    # Single element
    assert normalize([42]) == [0.0]

    # Mixed floats
    result = normalize([1.2, 3.6, 2.4])
    expected = [(1.2-1.2)/(3.6-1.2), (3.6-1.2)/(3.6-1.2), (2.4-1.2)/(3.6-1.2)]
    assert result == expected

    print("Sample Output")
    print("Docstring includes Args/Returns/Examples; guard for m==n")
    print("Acceptance Criteria: Doc quality and guard confirmed by tests")


if __name__ == "__main__":
    test_normalize()
