#!/usr/bin/env python3


class Employee(object):

    next_employee_number = 0

    def __init__(self, name, hours_worked=0.00,  hourly_rate=9.25):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        self.employee_number = Employee.next_employee_number
        Employee.next_employee_number += 1

    def __str__(self):
        l = []
        l.append('Name: {:s}'.format(self.name))
        l.append('ID: {:d}'.format(self.employee_number))
        l.append('Hours: {:.2f}'.format(self.hours_worked))
        l.append('Rate: {:.2f}'.format(self.hourly_rate))
        l.append('Wages: {:.2f}'.format(self.hours_worked * self.hourly_rate))
        return '\n'.join(l)

    def add_hours(self, hours):
        self.hours_worked += hours
