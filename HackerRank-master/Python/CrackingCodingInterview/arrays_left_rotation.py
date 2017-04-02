def array_left_rotation(a, n, k):
    for i in range(k):
        dequeued = a.pop(0)
        a.insert(len(a), dequeued)
    return a



n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(' '.join(map(str,answer)))
