import sys


class Matrix:
    def __init__(self, a):
        self.n = len(a)
        self.table = [[0 for _ in range(n)] for _ in range(n + 1)]
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
        bb = self.table[0][second]
        if a == 0:
            return
        if bb == 0:
            return
        ans = [0 for _ in range(n + 1)]
        ans[0] = a % bb
        k = a // bb
        self.add(first, second, -k)

    def gcd(self, first, second, f=True):
        if self.table[0][first] == 0:
            if f:
                self.add(first, second)
            return
        self.mod(second, first)
        self.gcd(second, first, False)
        if f and self.table[0][first] == 0:
            self.add(first, second)

    def println(self):
        for i in self.table:
            for j in i:
                print(j, end=' ')
            print()


n = 1
c = 0
m = Matrix([])
b = []
printing_zero = 0


def read():
    global n, m, b, printing_zero, c
    reentering = True
    aa = []
    while reentering:
        a = list(map(int, input("Enter coefficients you want to use: ").split()))
        n = len(a)
        c = int(input("What will on the right side of the equation?(It must be a number)\n"))
        print("The equation you entered is: ", end='')
        first_sign = False
        for i in range(n):
            if first_sign:
                if a[i] >= 0:
                    print(" + ", end='')
                else:
                    print(" - ", end='')
            else:
                first_sign = True
                if a[i] < 0:
                    print("-", end='')
            if abs(a[i]) != 1:
                print("{}*x_{}".format(abs(a[i]), i + 1), end='')
            else:
                print("x_{}".format(i + 1), end='')
        print("?[Y/n]")
        ans = input().lower()
        reentering = ans != 'y'
        if not reentering:
            aa = a.copy()
    printing_zero = input("Print terms with zero coefficient in the linear combination?[Y/n]\n").lower()
    printing_zero = bool(printing_zero == 'y')
    b = aa.copy()
    m = Matrix(aa)


def solve():
    for i in range(1, n):
        m.gcd(0, i)


def print_answer():
    print("GCD of all coefficients is {}.".format(m.table[0][0]))
    print("Linear combination: {} = ".format(m.table[0][0]), end='')
    print("{}*{}".format(m.table[1][0], b[0]), end='')
    for i in range(1, n):
        if m.table[i + 1][0] == 0 and not printing_zero:
            continue
        if m.table[i + 1][0] >= 0:
            print(" + ", end='')
        else:
            print(" - ", end='')
        print("{}*{}".format(abs(m.table[i + 1][0]), b[i]), end='')
    print()
    if c % m.table[0][0] != 0:
        print("This equation has no solutions")
    else:
        coefficient = c // m.table[0][0]
        for j in range(1, n + 1):
            print("x_{} = ".format(j), end='')
            first_sign = False
            if not(not printing_zero and m.table[j][0] == 0):
                print(m.table[j][0] * coefficient, end='')
                first_sign = True
            for i in range(1, n):
                if m.table[j][i] == 0 and not printing_zero:
                    continue
                if printing_zero or first_sign:
                    if m.table[j][i] >= 0:
                        print(" + ", end='')
                    else:
                        print(" - ", end='')
                else:
                    first_sign = True
                    if m.table[j][i] < 0:
                        print("-", end='')
                if abs(m.table[j][i]) * coefficient != 1:
                    print("{}*t_{}".format(abs(m.table[j][i]) * coefficient, i), end='')
                else:
                    print("t_{}".format(abs(i)), end='')
            print()


if __name__ == '__main__':
    sys.setrecursionlimit(int(1e6))
    read()
    solve()
    print_answer()
