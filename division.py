#!/usr/bin/env python
import argparse
import io 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        'Divide one number by another')
    parser.add_argument('numerator', type=float, help='Numerator')
    parser.add_argument('divisor', type=float, help='Divisor')
    
    args = parser.parse_args()
    try:
        print(args.numeratorwrweerwerwettewrtwtr / args.divisor)
    except:
        raise io.RumTimeError
