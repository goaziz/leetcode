from collections import Counter
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0

        while students and sandwiches:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                count = 0
            else:
                student = students.pop(0)
                students.append(student)
                count += 1

            if len(students) == count:
                break

        return count

    def countStudents2(self, students: List[int], sandwiches: List[int]) -> int:
        circle_student_count = 0
        square_student_count = 0

        # Count the number of students who want each type of sandwich
        for student in students:
            if student == 0:
                circle_student_count += 1
            else:
                square_student_count += 1

        # Serve sandwiches to students
        for sandwich in sandwiches:

            # No student wants the circle sandwich on top of the stack
            if sandwich == 0 and circle_student_count == 0:
                return square_student_count

            # No student wants the square sandwich on top of the stack
            if sandwich == 1 and square_student_count == 0:
                return circle_student_count

            # Decrement the count of the served sandwich type
            if sandwich == 0:
                circle_student_count -= 1
            else:
                square_student_count -= 1

        # Every student received a sandwich
        return 0


obj = Solution()
students = [1, 1, 1, 0, 0, 1]
sandwiches = [1, 0, 0, 0, 1, 1]
print(obj.countStudents2(students, sandwiches))
