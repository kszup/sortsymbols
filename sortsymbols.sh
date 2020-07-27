#!/bin/sh
grep -e "  Code  " -e "  Data  " $1 | awk -F0x '{print $2 " " $1 " " $3'} | sort
