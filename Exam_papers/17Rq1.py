def moo():
    s = "Summer_holidays"
    try:
        print(s[-2:-12:-2])
        i = len(s) // 2
        print(s[i:])
        s += '!'
        print(s)
    except:
        print('We have a problem')


def main():
    moo()

if __name__ == '__main__':
    main()
