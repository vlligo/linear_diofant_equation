import sys


class Matrix:
    def __init__(self, a):
        self.n = len(a)
        self.table = [[0 for j in range(n)] for i in range(n + 1)]
        for i in range(1, n + 1):
            self.table[i][i - 1] = 1
        self.table[0] = a

    def add(self, first, second, k=1):
        """Adds to first column second column multiplied on k"""
        if first < 0 or second < 0:
            return
        if first >= self.n or second >= self.n:
            return
        for i in range(self.n + 1):
            self.table[i][first] += self.table[i][second] * k

    def mod(self, first, second):
        if first < 0 or second < 0:
            return
        if first >= self.n or second >= self.n:
            return
        a = self.table[0][first]
        b = self.table[0][second]
        if a == 0:
            return
        if b == 0:
            return
        ans = [0 for i in range(n + 1)]
        ans[0] = a % b
        k = a // b
        self.add(first, second, -k)

    def swap(self, first, second):
        for i in range(self.n + 1):
            self.table[i][first], self.table[i][second] = self.table[i][second], self.table[i][first]

    def gcd(self, first, second, f=True):
        if self.table[0][first] == 0:
            if f:
                self.swap(first, second)
            return
        self.mod(second, first)
        self.gcd(second, first, False)
        if f and self.table[0][first] == 0:
            self.swap(first, second)

    def println(self):
        for i in self.table:
            for j in i:
                print(j, end=' ')
            print()


n = 1
m = Matrix([])
b = []
printing_zero = 0


def read():
    global n, m, b, printing_zero
    n = int(input())
    a = list(map(int, input().split()))
    printing_zero = input("Print terms with zero coefficient?[Y/n]\n").lower()
    printing_zero = bool(printing_zero == 'y')
    b = a.copy()
    m = Matrix(a)


def solve():
    for i in range(1, n):
        m.gcd(0, i)


def print_answer():
    print("{} = ".format(m.table[0][0]), end='')
    print("{}*{}".format(m.table[1][0], b[0]), end='')
    for i in range(1, n):
        if m.table[i + 1][0] == 0 and not printing_zero:
            continue
        if m.table[i + 1][0] >= 0:
            print(" + ", end='')
        else:
            print(" - ", end='')
        print("{}*{}".format(abs(m.table[i + 1][0]), b[i]), end='')
    for j in range(1, n):
        if m.table[1][j] >= 0:
            print(" + ")
        else:
            print(" - ")
        for i in range(1, n + 1):
            if m.table[i][j] == 0 and not printing_zero:
                continue
            if m.table[i][j] >= 0:
                print(" + ", end='')
            else:
                print(" - ", end='')
            print("{}*t_{}".format(abs(m.table[i][j]), j), end='')


if __name__ == '__main__':
    sys.setrecursionlimit(int(1e6))
    read()
    solve()
    print_answer()
