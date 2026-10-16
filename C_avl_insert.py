import sys


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.h = 1


def h(t):
    return t.h if t else 0


def upd(t):
    t.h = max(h(t.left), h(t.right)) + 1


def rot_left(a):
    b = a.right
    a.right = b.left
    b.left = a
    upd(a)
    upd(b)
    return b


def rot_right(a):
    b = a.left
    a.left = b.right
    b.right = a
    upd(a)
    upd(b)
    return b


def balance(t):
    upd(t)
    d = h(t.right) - h(t.left)
    if d == 2:
        if h(t.right.right) < h(t.right.left):
            t.right = rot_right(t.right)
        return rot_left(t)
    if d == -2:
        if h(t.left.left) < h(t.left.right):
            t.left = rot_left(t.left)
        return rot_right(t)
    return t


def add(t, x):
    if t is None:
        return Node(x)
    if x < t.key:
        t.left = add(t.left, x)
    elif x > t.key:
        t.right = add(t.right, x)
    else:
        return t
    return balance(t)


def exists(t, x):
    while t and t.key != x:
        t = t.left if x < t.key else t.right
    return t is not None


def preorder(t, res):
    if t:
        res.append(t.key)
        preorder(t.left, res)
        preorder(t.right, res)


lines = sys.stdin.read().split('\n')
root = None
out = []
for line in lines[1:]:
    cmd = line.split()
    if not cmd:
        continue
    if cmd[0] == 'add':
        root = add(root, int(cmd[1]))
    elif cmd[0] == 'exists':
        out.append('YES' if exists(root, int(cmd[1])) else 'NO')
    elif cmd[0] == 'root':
        out.append(str(root.key) if root else 'Empty')
    elif cmd[0] == 'height':
        out.append(str(h(root)))
    else:
        res = []
        preorder(root, res)
        out.append(' '.join(map(str, res)) if res else 'Empty')
print('\n'.join(out))
