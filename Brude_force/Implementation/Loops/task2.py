"""
Пошук всіх тризначних чисел, сума цифр яких дорівнює заданиму числу.
"""

if __name__ == '__main__':
    n = int(input())
    counter = 0

    for i in range(1, 10):
        for j in range(10):
            for k in range(10):
                if i + j + k == n:
                    counter += 1

    print(counter)
    