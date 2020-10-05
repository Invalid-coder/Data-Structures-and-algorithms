import math

def seconds(time):
    minutes,seconds = time.split(':')

    return int(minutes) * 60 + int(seconds)

def time(seconds):
    minutes = seconds // 60
    sec = seconds % 60

    if minutes < 10:
        minutes = '0' + str(minutes)

    if sec < 10:
        sec = '0' + str(sec)

    return '{}:{}'.format(minutes, sec)

def linear_search(array, v, d):
    t = 0
    prev = 0

    for dist, time_ in array:
        t += (int(dist) - prev) / v

        if t < seconds(time_):
            t += (seconds(time_) - t)

        t += d
        prev = int(dist)

    return math.ceil(t + int(array[-1][0]) / v)

if __name__ == '__main__':
    v,d = map(int, input().split())
    n = int(input())
    array = [input().split() for i in range(n)]
    print(time(linear_search(array, v, d)))


