from re import findall
import sys

from patterns_062 import date, phone


def main():

    # Verify regular expressions are not overly long
    assert(len(date) < 30)
    assert(len(phone) < 30)

    s = sys.stdin.read()

    datelist = findall(date, s)
    print('Dates: {}'.format(datelist))

    phonelist = findall(phone, s)
    print('Phones: {}'.format(phonelist))

    emaillist = findall(email, s)
    print('Emails: {}'.format(emaillist))

    ldatelist = findall(ldate, s)
    print('Long dates: {}'.format(ldatelist))

if __name__ == '__main__':
    main()
