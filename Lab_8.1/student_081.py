#!/usr/bin/env python3

from collections import namedtuple

Module = namedtuple('Module', 'code title ects')

CA1_MODULES = {'CA103': Module('CA103', 'Computer Systems', 5),
               'CA106': Module('CA106', 'Web Design', 5),
               'CA115': Module('CA115', 'Digital Innovation', 5),
               'CA116': Module('CA116', 'Computer Programming I', 10),
               'CA117': Module('CA117', 'Computer Programming II', 10),
               'CA169': Module('CA169', 'Networks and Internet', 5),
               'CA170': Module('CA170', 'Operating Systems', 5),
               'CA172': Module('CA172', 'Problem Solving', 5),
               'MS121': Module('MS121', 'IT Mathematics', 10)}


class Student(object):

    def __init__(self, idnum, surname, firstname, mods=CA1_MODULES):
        self.__idnum = idnum
        self.__surname = surname
        self.__firstname = firstname
        self.__mods = mods
        self.__marks = {code: 0 for code in self.__mods.keys()}

    def __str__(self):
        name = '{} : {} {}'.format(self.__idnum,
                                   self.__firstname,
                                   self.__surname)
        uline = '-' * len(name)
        results = '\n'.join([code + ' : ' + self.__mods[code].title +
                             ' : ' + str(self.__marks[code])
                             for code in sorted(self.__mods.keys())])
        pm = 'Precision mark: {:.2f}'.format(self.precision_mark())
        if self.passed():
            outcome = 'Pass'
        elif self.passed_by_compensation():
            outcome = 'Pass by compensation'
        else:
            outcome = 'Fail'

        return '\n'.join([name, uline, results, pm, outcome])

    def add_mark(self, module, mark):
        self.__marks[module] = mark

    def precision_mark(self):
        total = 0
        self.__ten_creds = ['CA116', 'CA117', 'MS121']
        for k, v in self.__marks.items():
            if k in self.__ten_creds:
                weight = 1 / 6
                grade = v / 100
                weighted_mark = grade * weight
                total += weighted_mark
            else:
                weight = 1 / 12
                grade = v / 100
                weighted_mark = grade * weight
                total += weighted_mark
        precision_mark = total * 100
        return precision_mark

    def passed(self):
        self.__failed_mods = []
        self.__failed_creds = 0
        for k, v in self.__marks.items():
            if v < 40:
                if k in self.__ten_creds:
                    self.__failed_creds += 10
                else:
                    self.__failed_creds += 5
                self.__failed_mods.append(k)
                return False
        return True

    def passed_by_compensation(self):
        for mod in self.__failed_mods:
            if self.__marks[mod] < 35:
                return False
        if self.precision_mark() >= 45 and self.__failed_creds / 60 <= 1 / 6:
            return True
