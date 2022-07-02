import sys

def less(name, n):
    f = open(name, 'r')
    for l in f:
        while n >= 0:
            if n > 0:
                print(l)
            else:
                print(l, end='')
            l = next(f);
            n -= 1
        s = input()
        if(s == 'q'):
            break
        print(l, end='')

less(sys.argv[1], int(sys.argv[2]))
