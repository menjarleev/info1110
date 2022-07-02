import sys

def tape_read(f, n):
    b = f.read(n)
    print(b)

def tape_move(f, offset):
    pos = f.tell()
    f.seek(pos+offset, 0)

def tape_load(filename):
    return open(filename, 'r')

def ask_user(tape):
    s = input()
    if s.startswith('MOVE'):
        sp = s.split()
        tape_move(tape, int(sp[1]))
        return True
    if s.startswith('READ'):
        sp = s.split()
        tape_read(tape, int(sp[1]))
        return True
    if s == 'QUIT':
        return False

tape = tape_load(sys.argv[1])
work = True
while work:
    work = ask_user(tape)
