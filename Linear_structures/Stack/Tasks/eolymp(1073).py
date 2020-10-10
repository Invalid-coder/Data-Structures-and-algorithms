#https://www.e-olymp.com/uk/submissions/7479745

def toString(coefitients):
    result = ""

    for i in range(10, 0, - 1):
        if coefitients[i] != 0:
            if coefitients[i] == 1:
                result += "n"
            elif coefitients[i] == -1:
                result += "-n"
            else:
                result += "{}*n".format(str(coefitients[i]))

            if i != 1:
                result += "^{}".format(i)

        if coefitients[i - 1] > 0 and result:
            result += "+"

    if not result or coefitients[0] != 0:
        result += str(coefitients[0])

    return result

if __name__ == '__main__':
    with open("input.txt") as inp:
        text = inp.readlines()
        n = int(text[0].rstrip())
        i = 1

        for k in range(1, n + 1):
            coefitients = [0] * 11
            keywords = 0
            params = []
            #for BEGIN
            params.append(1)
            keywords += 1
            j = 1

            while keywords != 0:
                line = text[i].lstrip().rstrip().split()

                while j < len(line):
                    if line[j] == "LOOP":
                        keywords += 1
                        j += 1
                        params.append(line[j])
                    elif line[j] == "OP":
                        j += 1
                        num = int(line[j])
                        multiplier = 1
                        pow = 0

                        for param in params:
                            if param == "n":
                                pow += 1
                            else:
                                multiplier *= int(param)

                        coefitients[pow] += multiplier * num
                    elif line[j] == "END":
                        keywords -= 1
                        params.pop()

                    j += 1

                i += 1
                j = 0

            print("Program #{}".format(k))
            print("Runtime = {}".format(toString(coefitients)))

            if k < n:
                print()
                i += 1

"""
class Stack():
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def back(self):
        return self.items[-1]

    def pop(self):
        return self.items.pop()

class Polinom():
    def __init__(self):
        self.values = [0]

    def __iadd__(self, other):
        if isinstance(other, str):
            self.values[0] += int(other)
        else:
            if len(other.values) > len(self.values):
                for i in range(len(self.values)):
                    other.values[i] += self.values[i]

                return other
            else:
                for i in range(len(other.values)):
                    self.values[i] += other.values[i]

        return self

    def __imul__(self, other):
        if other.isdigit():
            self.values = list(map(lambda x: x * int(other), self.values))
        else:
            self.values.insert(0, 0)

        return self

    def __str__(self):
        s = ""

        if len(self.values) == 1:
            return str(self.values[0])

        for i in range(len(self.values) - 1, 1, -1):
            if self.values[i] > 0:
                if self.values[i] > 1:
                    s += "{}*n^{}+".format(self.values[i], i)
                else:
                    s += "n^{}+".format(i)

        if self.values[1] > 0:
            if self.values[1] > 1:
                s += "{}*n+".format(self.values[1])
            else:
                s += "n+"

        if self.values[0] > 0:
            s += str(self.values[0])
        else:
            s = s[:-1]

        return s

if __name__ == '__main__':
    stack = Stack()

    with open("input.txt") as inp:
        text = inp.readlines()
        k = int(text[0].rstrip())
        i = 1
        j = 1

        while i < len(text):
            command = text[i].rstrip().lstrip()

            if command != "":
                command = command.split()
            else:
                i += 1
                continue

            if command[0] == "END":
                it = stack.pop()
                p = Polinom()

                while it[0] != "LOOP":
                    if it[0] == "BEGIN":
                        print("Program #{}".format(j))
                        print("Runtime = {}".format(p))

                        if j < k:
                            print()

                        j += 1

                        break

                    p += it[1]

                    it = stack.pop()

                if it[0] != "BEGIN":
                    p *= it[1]

                    stack.push(("RESULT", p))
            else:
                stack.push(command)

            i += 1
"""