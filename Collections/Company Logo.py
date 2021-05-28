#!/bin/python3
from collections import Counter
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = Counter(sorted(input().strip()))
    e=s.most_common(3)
    for x in e:
        print(*x)
