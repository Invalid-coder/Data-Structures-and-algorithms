maxProduct = 0

def findMaxProduct(product, number, chunk_num):
    global maxProduct

    if len(number) == 0:
        return
    elif len(number) == 1:
        chunk_num += 1
        product *= int(number)
        number = ''

    if chunk_num == m:
        if product > maxProduct:
            maxProduct = product

        return

    for i in range(1, len(number)):
        if chunk_num + 1 + len(number[i:]) < m:
            continue

        findMaxProduct(product * int(number[:i]), number[i:], chunk_num + 1)

if __name__ == '__main__':
    with open("input.txt") as inp:
        for line in inp.readlines():
            n, m = map(int, line.rstrip().split())
            findMaxProduct(1, str(n), 0)
            
            print(maxProduct)

            maxProduct = 0
