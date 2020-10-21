#https://www.e-olymp.com/uk/submissions/7100353

class Worker():
    def __init__(self, name):
        self.name = name
        self.supervisors = []

    def getName(self):
        return self.name

    def addSupervisor(self, name):
        self.supervisors.append(name)

    def getSupervisors(self):
        return self.supervisors

class DataBase():
    def __init__(self, n):
        self.top = []
        self.staff = {}
        self.initDadaBase(n)

    def initDadaBase(self, n):
        for i in range(n):
            self.addWorker(i)

    def addWorker(self, name):
        worker = Worker(name)
        self.staff[name] = worker

    def getWorker(self, name):
        return self.staff[name]

    def dfs(self, worker, used):
        used[worker.getName()] = True;

        for w in worker.getSupervisors():
            if not used[w.getName()]:
                self.dfs(w, used)

        self.top.append(worker)

    def __getitem__(self, name):
        return self.getWorker(name)


if __name__ == '__main__':
    n,m = map(int, input().split())
    dataBase = DataBase(n)
    commands = [[0]*5 for i in range(n)]
    ans = [0 for i in range(n)]
    used = [False for i in range(n)]

    for i in range(m):
        x,y = map(int, input().split())
        x, y = x - 1, y - 1
        dataBase[y].addSupervisor(dataBase[x])

    k = int(input())

    for i in range(k):
        t, x = map(int, input().split())
        t, x = t - 1, x - 1
        commands[x][t] = i + 1

    for i in range(n):
        if not used[dataBase[i].getName()]:
            dataBase.dfs(dataBase.getWorker(i), used)

    for i in range(n):
        top = dataBase.top[i]

        for w in top.getSupervisors():
            commands[top.getName()][3] = max(commands[top.getName()][3], commands[w.getName()][3])

        ans[top.getName()] |= (commands[top.getName()][0] > commands[top.getName()][1])

        for w in top.getSupervisors():
            ans[top.getName()] |= (ans[w.getName()] and (max(commands[w.getName()][2],commands[w.getName()][3]) > commands[w.getName()][4]))

    for i in range(n):
        print(ans[i], end=' ')
