import sys
sys.setrecursionlimit(10000)


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def add(t, x):
    if t is None:
        return Node(x)
    if x < t.key:
        t.left = add(t.left, x)
    else:
        t.right = add(t.right, x)
    return t


def rot_left(a):
    b = a.right
    a.right = b.left
    b.left = a
    return b


def rot_right(a):
    b = a.left
    a.left = b.right
    b.right = a
    return b


def turn(t, x, f):
    if t.key == x:
        return f(t)
    if x < t.key:
        t.left = turn(t.left, x, f)
    else:
        t.right = turn(t.right, x, f)
    return t


def preorder(t, res):
    if t:
        res.append(t.key)
        preorder(t.left, res)
        preorder(t.right, res)


data = sys.stdin.read().split()
n = int(data[0])
root = None
for x in data[1:n + 1]:
    root = add(root, int(x))
m = int(data[n + 1])
out = []
for i in range(m):
    d = data[n + 2 + 2 * i]
    x = int(data[n + 3 + 2 * i])
    root = turn(root, x, rot_left if d == 'left' else rot_right)
    res = []
    preorder(root, res)
    out.append(' '.join(map(str, res)))
print('\n'.join(out))
