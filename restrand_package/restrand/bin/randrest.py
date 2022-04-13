#!/usr/bin/env python
import sys
import random

def add(args):
    filename = args.infile
    name = args.add
    my_file = open(''.join(filename),'r')
    f = my_file.read()
    my_file.close()
    content = f.split(',')
    for c in content:
        if c == name:
            print('the restaurant is already in list')
            return
    
    content.append(name)
    res = ''
    for c in content:
        if len(res) != 0 :
            res += ','
        res += c

    my_file = open(''.join(filename),'w')
    my_file.write(res)
    print(f'Updated restaurant list is: {content}')

def remove(args):
    filename = args.infile
    name = args.remove
    my_file = open(''.join(filename),'r')
    f = my_file.read()
    my_file.close()
    content = f.split(',')
    content_new = []
    for c in content:
        if c != name:
            content_new.append(c)
    
    res = ''
    for c in content_new:
        if len(res) != 0 :
            res += ','
        res += c

    my_file = open(''.join(filename),'w')
    my_file.write(res)
    print(f'Updated restaurant list is: {content_new}')

def show(args):
    filename = args.infile
    name = args.remove
    my_file = open(''.join(filename),'r')
    f = my_file.read()
    my_file.close()
    print(f)

def pick():
    filename = sys.argv[1]
    my_file = open(filename,'r')
    f = my_file.read()
    content = f.split(",")
    s = len(content)
    ind =random.randint(0, s-1)
    my_file.close()
    return content[ind]

def choose(args):
    filename = args.infile
    ind = args.choose
    my_file = open(''.join(filename),'r')
    f = my_file.read()
    my_file.close()
    content = f.split(',')
    leng = len(content)
    if ind > leng:
        print('Index out of range!')
        return
    print(f'Picked restaurant is: {content[ind-1]}')
    


def main(args):
    if args.infile == '-':
        print('please specify or provide a restaurant list, seperated by comma')
        return
    if args.add:
        print(f'add a restaurant: {args.add}')
        add(args)
    elif args.remove:
        print(f'remove a restaurant: {args.remove}')
        remove(args)
    elif args.s:
        print('show all the restaurant in the list')
        show(args)
    elif args.choose:
        choose(args)
    else:
        print(f'Picked restaurant is {pick()}')
    
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='collate')
    parser.add_argument('-a', '--add', type=str, help='add a restaurant')
    parser.add_argument('-r', '--remove', type=str, help='remove a restaurant')
    parser.add_argument('-c', '--choose', type=int, help='(Cheating) pick the specific one (1 indexed)')
    parser.add_argument('-s', action='store_true', help='Show the list')
    parser.add_argument('infile', type=str, nargs='*', default='-',
                        help='Input file name(s)')
    args = parser.parse_args()
    main(args)