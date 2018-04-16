class Triathlete(object):
 
    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
 
    def __str__(self):
        r = []
        r.append('Name: {:s}'.format(self.name))
        r.append('ID: {:d}'.format(self.tid))
        return '\n'.join(r)
 
def sort_on(t):
    return t.name

class Triathlon(object):

    def __init__(self):
        self.d = {}

    def add(self, s):
        self.d[s.tid] = s

    def remove(self, tid):
        del(self.d[tid])

    def lookup(self, tid):
        if tid in self.d:
            return self.d[tid]
        else:
            return None

    def __str__(self):
        slist = ['{}'.format(t) for t in sorted(self.d.values(), key=sort_on)]
        return '\n'.join(slist)