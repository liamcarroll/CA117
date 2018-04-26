def display(d):
    for e in sorted(d.items(), key=lambda x: x[1]):
        print('{:s}: {:d}'.format(e[0], e[1]))


def main():
    d = {'bananas': 5, 'apples': 8, 'oranges': 1, 'pears': 4}
    display(d)

if __name__ == '__main__':
    main()
