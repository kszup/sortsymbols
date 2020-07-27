#!/usr/bin/env python3
# coding=utf-8
"""This script sorts symbols in an IAR .MAP file."""

# sortsymbols.py - Sort Symbols in IAR .MAP file.
# https://github.com/kszup/sortsymbols.git

import sortSymbolsHelper as h

VERSION = "0.1"

def main():
    lines = h.get_data('mymp.map')
    symbols = h.get_symbols(lines)
    clean_symbols = h.clean_data(lines,symbols)
    sorted_symbols = h.sort_data(clean_symbols)
    f = open('output.txt','w')
    for x in sorted_symbols: f.write(x)
    # 


if __name__ == "__main__":
    main()
