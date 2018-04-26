from queue import Queue


def reorder(q):
    evens = [n for n in q.l if not n % 2]
    odds = [n for n in q.l if n % 2]
    new_l = evens + odds
    new_q = Queue(new_l)
    return new_q

q = Queue([4, 1, 3, 6, 8, 10])
new_q = reorder(q)
print(new_q.l)
