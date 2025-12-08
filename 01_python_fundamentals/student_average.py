"""
Problem
-------
Store student marks in a dictionary and compute the average marks
for a queried student.

Concepts Practiced
------------------
- Dict of name -> list of scores
- Splitting and mapping input
- Using sum() and len() safely
"""


def average(scores: list[float]) -> float:
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


if __name__ == "__main__":
    n = int(input("Number of students: "))
    student_marks: dict[str, list[float]] = {}

    for _ in range(n):
        name, *line = input("Enter name and scores: ").split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input("Student to query: ").strip()
    query_scores = student_marks.get(query_name, [])
    print(average(query_scores))

