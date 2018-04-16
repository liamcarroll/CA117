class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        l = []
        l.append('Name: {:s}'.format(self.name))
        l.append('ID: {:d}'.format(self.tid))
        return '\n'.join(l)


class Triathlon(object):

    def __init__(self):
        self.mapping = {}

    def __str__(self):
        l = []
        for e in sorted(self.mapping.values(), key=lambda x: x.name):
            l.append('Name: {:s}'.format(e.name))
            l.append('ID: {:d}'.format(e.tid))
        return '\n'.join(l)

    def add(self, triathlete):
        self.mapping[triathlete.tid] = triathlete

    def remove(self, tid):
        del(self.mapping[tid])

    def lookup(self, tid):
        if tid in self.mapping:
            return self.mapping[tid]
        return None
