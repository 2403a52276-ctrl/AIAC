from typing import List

class Student:
    """Represent a student with name, age and marks.

    Attributes:
        name (str): Student's full name.
        age (int): Student's age.
        marks (List[float]): List of numeric marks.
    """

    def __init__(self, name: str, age: int, marks: List[float]):
        self.name = name
        self.age = int(age)
        # store marks as a list so we can use sum(self.marks)
        self.marks = [float(m) for m in marks]

    def details(self) -> None:
        """Print a readable summary of the student's details and marks."""
        marks_str = ", ".join(f"{m:.1f}" for m in self.marks)
        print(
            f"Name: {self.name} | Age: {self.age} | Marks: [{marks_str}] "
            f"| Total: {self.total():.1f} | Average: {self.average():.2f}"
        )

    def total(self) -> float:
        """Return the total of the student's marks."""
        return sum(self.marks)

    def average(self) -> float:
        """Return the average mark (0.0 when there are no marks)."""
        return self.total() / len(self.marks) if self.marks else 0.0

    def add_mark(self, mark: float) -> None:
        """Add a new mark to the student's marks."""
        self.marks.append(float(mark))

    def __repr__(self) -> str:
        return f"Student(name={self.name!r}, age={self.age}, marks={self.marks})"


if __name__ == "__main__":
    # simple demonstration
    s = Student("Alice", 20, [78, 85, 92])
    s.details()