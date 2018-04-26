class Queue(object):

    def __init__(self, l=[]):
        self.l = l

    def __len__(self):
        return len(self.l)

    def enqueue(self, e):
        self.l.append(e)

    def dequeue(self):
        top = self.l[0]
        self.l = self.l[1:]
        return top

    def first(self):
        return self.l[0]

    def is_empty(self):
        if not len(self):
            return True
        return False
