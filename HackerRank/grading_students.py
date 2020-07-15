def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] >= 38 and grades[i] % 5 > 2:
            grades[i] = grades[i] + (5 - (grades[i] % 5))

    return grades