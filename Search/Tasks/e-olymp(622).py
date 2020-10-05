#https://www.e-olymp.com/uk/submissions/7169882

def binary_digits(num):
    counter = 0

    while num > 1:
        if num % 2 == 1:
            counter += 1

        num //= 2

    return counter + 1

if __name__ == '__main__':
    num = int(input())
    print(binary_digits(num))
