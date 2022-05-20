grades = []
#fadksnvjwad

def displayGrades():
    print(grades)


def addGrades():
    while True:
        grade = int(input("Enter a Grade: "))
        if grade == -1:
            break
        else:
            grades.append(grade)


def averageGrade():
    sum = 0
    for i in grades:
        sum += i
    return sum / len(grades)


def roundUpGrades():
    for i in range(len(grades)):
        if grades[i] == 69 or grades[i] == 79 or grades[i] == 89:
            grades[i] += 1


def removeLowGrade():
    low = grades[0]
    for g in grades:
        if g < low:
            low = g
    grades.remove(low)


# tester code
addGrades()
roundUpGrades()
removeLowGrade()
displayGrades()
print("Average: " + str(averageGrade()))
