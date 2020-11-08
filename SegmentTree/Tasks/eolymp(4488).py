#https://www.e-olymp.com/uk/submissions/7669637

if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    m = int(input())

    for _ in range(m):
        data = list(map(int, input().split()))
        data[1] -= 1

        if data[0] == 1:
            max_count = 0
            counter = 1
            prev = array[data[1]]

            for i in range(data[1] + 1, data[2]):
                if array[i] >= prev:
                    counter += 1
                else:
                    max_count = max(max_count, counter)
                    counter = 1

                prev = array[i]

            print(max(max_count, counter))
        else:
            for i in range(data[1], data[2]):
                array[i] = data[3]