my_dict = {}

def addTranslation(eng, translation):
    if not eng in my_dict:
        my_dict[eng] = [translation]
    else:
        my_dict[eng].append(translation)

def find(eng):
    return ' '.join(sorted(my_dict[eng])) if eng in my_dict else ''

if __name__ == '__main__':
    data = input()

    while data:
        eng,trans = data.split(' - ')
        addTranslation(eng, trans)
        data = input()

    print(find(input()))