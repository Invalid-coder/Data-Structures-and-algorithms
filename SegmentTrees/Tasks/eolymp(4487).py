#https://www.e-olymp.com/uk/submissions/7669466

if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    m = int(input())

    for _ in range(m):
        q, l, r = map(int, input().split())
        l -= 1

        if q == 1:
            max_count = 0
            counter = 1
            prev = array[l]

            for i in range(l + 1, r):
                if array[i] >= prev:
                    counter += 1
                else:
                    max_count = max(max_count, counter)
                    counter = 1

                prev = array[i]

            print(max(max_count, counter))
        else:
            array[l] = r