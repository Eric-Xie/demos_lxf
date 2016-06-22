# -*- coding: utf-8 -*-

from datetime import datetime
import os

def main():
    print("Demo for ls -l")
    pwd = os.path.abspath('.')
    print("Current path: %s" % pwd)

    print('      Size     Last Modified  Name')
    print('-'*60)

    for f in os.listdir(pwd):
        fsize = os.path.getsize(f)
        mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
        flag = '/' if os.path.isdir(f) else ''
        print('%10d  %s  %s%s' % (fsize, mtime, f, flag))


if __name__ == '__main__':
    main()