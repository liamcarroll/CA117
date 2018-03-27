#!/usr/bin/env python3


class BankAccount(object):

    next_account_number = 16555232
    total_lodgements = 0
    interest_rate = 0.043

    def __init__(self, forename, surname, balance=0.00):
        self.forename = forename
        self.surname = surname
        self.balance = balance
        self.account_number = BankAccount.next_account_number
        BankAccount.next_account_number += 1

    def __str__(self):
        l = []
        name = self.forename + ' ' + self.surname
        l.append('Name: {:s}'.format(name))
        l.append('Account number: {:d}'.format(self.account_number))
        l.append('Balance: {:.2f}'.format(self.balance))
        return '\n'.join(l)

    def __iadd__(self, amount):
        self.balance += amount
        BankAccount.total_lodgements += 1
        return self

    def lodge(self, amount):
        self.balance += amount
        BankAccount.total_lodgements += 1

    def apply_interest(self):
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
