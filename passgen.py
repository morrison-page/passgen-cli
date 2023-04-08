#!/usr/bin/env python3

import sys
import argparse
import random
import string

def generate_password(length, lowercase, uppercase, digits, punctuation):
    charset = ''
    if lowercase:
        charset += string.ascii_lowercase
    if uppercase:
        charset += string.ascii_uppercase
    if digits:
        charset += string.digits
    if punctuation:
        charset += string.punctuation
    if not charset:
        raise ValueError('At least one character set must be selected. Use --lowercase, --uppercase, --digits, and/or --punctuation options.')
    password = ''.join(random.choice(charset) for _ in range(length))
    return password


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--length', type=int, default=12)
    parser.add_argument('--lowercase', action='store_true')
    parser.add_argument('--uppercase', action='store_true')
    parser.add_argument('--digits', action='store_true')
    parser.add_argument('--punctuation', action='store_true')
    args = parser.parse_args()

    try:
        password = generate_password(args.length, args.lowercase, args.uppercase, args.digits, args.punctuation)
    except ValueError as e:
        print(str(e))
        return

    print(password)

if __name__ == '__main__':
    sys.exit(main())
