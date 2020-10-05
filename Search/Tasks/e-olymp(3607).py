if __name__ == '__main__':
    n = input()
    array = list(map(int, input().split()))
    a, b = map(int, input().split())
    counter = 0

    for el in array:
        if a <= el <= b:
            counter += 1

    print(counter)