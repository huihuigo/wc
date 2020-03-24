import re
import os
import sys


def count_char(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
            return len(text)
    except FileNotFoundError:
        print('%s does not exist' % filename)


def count_word(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
            words = re.split(r'\W+', text)
            if words[-1] == "":
                return len(words) - 1
            return len(words)
    except FileNotFoundError:
        print('%s does not exist' % filename)


def count_line(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            return len(lines)
    except FileNotFoundError:
        print('%s does not exist' % filename)


def count_dir(dirname):
    try:
        for x in os.listdir(dirname):
            if os.path.isdir(dirname + '\\' + x):
                count_dir(dirname + '\\' + x)
            elif os.path.isfile(dirname + '\\' + x) and os.path.splitext(dirname + '\\' + x)[1] == '.c':
                print(dirname + '\\' + x, '字符数, 词数, 行数: ', end='')
                print(count_char(dirname + '\\' + x), count_word(dirname + '\\' + x), count_line(dirname + '\\' + x))
    except FileNotFoundError:
        print('%s does not exist' % dirname)


def count_all(filename):
    codeline = 0
    expline = 0
    blankline = 0
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            while f.tell() != os.path.getsize(filename):
                line = f.readline().strip()
                if line == '' or len(line) == 1:
                    blankline += 1
                elif line.startswith('//'):
                    expline += 1
                elif line.startswith('/*'):
                    expline += 1
                    while True:
                        temp = f.readline().strip()
                        expline += 1
                        if temp.endswith('*/'):
                            break
                else:
                    codeline += 1
        return blankline, codeline, expline
    except FileNotFoundError:
        print('%s does not exist' % filename)


if __name__ == '__main__':
    choice = sys.argv[1]
    filename = sys.argv[2]
    if choice == '-c':
        print('字符数: ', count_char(filename))
    elif choice == '-w':
        print('词数: ', count_word(filename))
    elif choice == '-l':
        print('行数: ', count_line(filename))
    elif choice == '-s':
        count_dir(filename)
    elif choice == '-a':
        blankline, codeline, expline = count_all(filename)
        print('空行: ', blankline)
        print('代码行: ', codeline)
        print('注释行: ', expline)
