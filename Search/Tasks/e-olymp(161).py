def getMinTime(d, r_a, r_b):
    rob_a = {i:i for i in r_a}
    rob_b = {i:i for i in r_b}
    details = [[False, False] for i in range(d)]
    processing = [[None, None] for i in range(d)]
    time = 0

    while details:
        done = []

        for i in range(len(details)):
            if not details[i][0]:
                if not processing[i][1]:
                    if not processing[i][0]:
                        for k, v in rob_a.items():
                            if k == v:
                                processing[i][0] = k
                                rob_a[k] -= 1
                                break
                    else:
                        if rob_a[processing[i][0]]:
                            rob_a[processing[i][0]] -= 1
                        else:
                            details[i][0] = True
                            rob_a[processing[i][0]] = processing[i][0]
                            processing[i][0] = None

            if not details[i][1]:
                if not processing[i][0]:
                    if not processing[i][1]:
                        for k, v in rob_b.items():
                            if k == v:
                                processing[i][1] = k
                                rob_b[k] -= 1
                                break
                    else:
                        if rob_b[processing[i][1]]:
                            rob_b[processing[i][1]] -= 1
                        else:
                            details[i][1] = True
                            rob_b[processing[i][1]] = processing[i][1]
                            processing[i][1] = None

            if details[i][0] and details[i][1]:
                done.append(i)

        i = 0

        for j in done:
            del details[j - i]
            del processing[j - i]

            i += 1

        time += 1

    return time


if __name__ == '__main__':
    d = int(input())
    a = input()
    r_a = list(map(int, input().split()))
    b = input()
    r_b = list(map(int, input().split()))

    print(getMinTime(d, r_a, r_b))







class Detail():
    def __init__(self):
        self.a = False
        self.b = False


class Robot():
    def __init__(self, type, time):
        self.type = type
        self.time = time
        self.process = time
        self.detail = None

    def print(self):
        print(self.type, self.time)

def getKey(obj):
    return obj.time

def getAns(n, t_a, t_b):
    t_a, t_b = sorted(t_a), sorted(t_b)
    details = [Detail() for i in range(n)]
    robotsA = [Robot('A', time) for time in t_a]
    robotsB = [Robot('B', time) for time in t_b]
    time = 0
    processRobots = []

    while n != 0:
        robotsA = sorted(robotsA, key=getKey)
        robotsB = sorted(robotsB, key=getKey)

        if details:
            robot = None
            detail = details.pop(0)

            if (detail.b or not detail.b) and not detail.a:
                if robotsA:
                    robot = robotsA.pop(0)
            elif (detail.a or not detail.a) and not detail.b:
                if robotsB:
                    robot = robotsB.pop(0)

            if robot:
                robot.detail = detail
                processRobots.append(robot)
            else:
                details.append(detail)

        for robot in processRobots:
            #print(robot.time)
            robot.process -= 1

            if robot.process == 0:
                robot.process = robot.time

                if robot.type == 'A':
                    robot.detail.a = True
                    robotsA.append(robot)
                else:
                    robot.detail.b = True
                    robotsB.append(robot)

                if robot.detail.a and robot.detail.b:
                    n -= 1
                else:
                    details.append(robot.detail)
                    robot.detail = None

                processRobots.pop(processRobots.index(robot))
        time += 1

    print(time)


if __name__ == '__main__':
    n = int(input())
    a = int(input())
    t_a = list(map(int, input().split()))
    b = int(input())
    t_b = list(map(int, input().split()))
    getAns(n, t_a, t_b)