# -*- coding: utf-8 -*-
import os
import sys

def main():
    curr_dir = os.path.abspath(os.path.dirname(__file__))
    binary = os.path.join(curr_dir, 'rdb-binary', 'rdb')
    return os.execv(binary, sys.argv)


if __name__ == '__main__':
    main()
