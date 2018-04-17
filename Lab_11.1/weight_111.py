class Weight(object):

    OUNCES_PER_POUND = 16

    def __init__(self, pounds=0, ounces=0):
        self.pounds = pounds
        self.ounces = ounces

    def from_ounces(ounces):
        pounds, ounces = divmod(ounces, 16)
        return Weight(pounds, ounces)

    def __str__(self):
        return '{:d} pounds(s) and {:d} ounce(s)'.format(self.pounds, self.ounces)

    def pounds_to_ounces(self):
        return (self.pounds * 16) + self.ounces

    def __ne__(self, other):
        return self.pounds_to_ounces != other.pounds_to_ounces

    def __eq__(self, other):
        return self.pounds_to_ounces == other.pounds_to_ounces

    def __lt__(self, other):
        return self.pounds_to_ounces < other.pounds_to_ounces

    def __gt__(self, other):
        return self.pounds_to_ounces > other.pounds_to_ounces

    def __ge__(self, other):
        return self.pounds_to_ounces >= other.pounds_to_ounces

    def __add__(self, other):
        (self.pounds_to_ounces + other.pounds_to_ounces)
