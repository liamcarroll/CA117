from queue import Queue


def main():

    q = Queue()
    print(len(q))
    q.enqueue(1)
    q.enqueue(2)
    print(q.first())
    print(q.is_empty())
    print(len(q))
    print(q.dequeue())
    print(q.dequeue())
    print(q.is_empty())
    print(len(q))
    try:
        print(q.dequeue())
    except IndexError:
        print('Error')
    try:
        print(q.first())
    except IndexError:
        print('Error')

if __name__ == '__main__':
    main()
