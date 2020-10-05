#https://www.e-olymp.com/uk/submissions/7298642

def greaterClass(a, b):
    cls1 = (int(a[0][:-1]), a[0][-1])
    cls2 = (int(b[0][:-1]), b[0][-1])

    if cls1[0] > cls2[0]:
        return a
    elif cls1[0] < cls2[0]:
        return b
    else:
        if ord(cls1[1]) > ord(cls2[1]):
            return a
        else:
            return b

def lexicographically_greater(a, b):
    i = 0
    j = 0
    surname1, surname2 = a[1], b[1]

    while i < len(surname1) and j < len(surname2):
        if ord(surname1[i]) > ord(surname2[j]):
            return a
        elif ord(surname1[i]) < ord(surname2[j]):
            return b
        else:
            i += 1
            j += 1

    if len(surname1) > len(surname2):
        return a
    else:
        return b

def greater(a, b):
    if a[0] != b[0]:
        return greaterClass(a, b)
    else:
        return lexicographically_greater(a, b)

def bubble_sort(array):
    n = len(array)

    for pass_num in range(n - 1, 0, -1):
        isSorted = True

        for i in range(pass_num):
            if greater(array[i], array[i + 1]) == array[i]:
                array[i], array[i + 1] = array[i + 1], array[i]
                isSorted = False

        if isSorted:
            break

if __name__ == '__main__':
    N = int(input())
    students = []

    for i in range(N):
        surname = input()
        name = input()
        class_ = input()
        birthday = input()
        students.append((class_, surname, name, birthday))

    bubble_sort(students)

    for student in students:
        print(*student)
