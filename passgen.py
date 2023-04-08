#!/usr/bin/env python3

import sys
import argparse
import random
import string

def generate_password(length):
    charset = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(charset) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--length', type=int, default=12)
    args = parser.parse_args()
    password = generate_password(args.length)
    print(password)

if __name__ == '__main__':
    sys.exit(main())

# Fucntionality to add later #
# number of passwords to generate
# lowercase only
# uppercase only
# a man page
