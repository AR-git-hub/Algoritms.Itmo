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
    elif x > t.key:
        t.right = add(t.right, x)
    return t


def remove(t, x):
    if t is None:
        return None
    if x < t.key:
        t.left = remove(t.left, x)
    elif x > t.key:
        t.right = remove(t.right, x)
    else:
        if t.left is None:
            return t.right
        if t.right is None:
            return t.left
        m = t.right
        while m.left:
            m = m.left
        t.key = m.key
        t.right = remove(t.right, m.key)
    return t


def exists(t, x):
    while t and t.key != x:
        t = t.left if x < t.key else t.right
    return t is not None


def height(t):
    if t is None:
        return 0
    return max(height(t.left), height(t.right)) + 1


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
    elif cmd[0] == 'del':
        root = remove(root, int(cmd[1]))
    elif cmd[0] == 'exists':
        out.append('YES' if exists(root, int(cmd[1])) else 'NO')
    elif cmd[0] == 'height':
        out.append(str(height(root)))
    else:
        res = []
        preorder(root, res)
        out.append(' '.join(map(str, res)) if res else 'Empty')
print('\n'.join(out))
