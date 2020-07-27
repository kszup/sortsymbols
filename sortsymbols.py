#!/usr/bin/env python3
# coding=utf-8
"""This script sorts symbols in IAR .MAP file."""

# sortsymbols.py - Sort Symbols in IAR .MAP file.
# https://github.com/kszup/sortsymbols.git

import ssHelper as h

VERSION = "0.1"

def main():
    lines = h.get_data('mp.map')
    symbols = h.get_symbols(lines)
    clean_symbols = h.clean_data(lines,symbols)
    f = open('output.txt','w')
    for x in clean_symbols: f.write(x)
    # 


if __name__ == "__main__":
    main()
