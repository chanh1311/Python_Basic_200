#!/bin/python3

import math
import os
import random
import re
import sys


N, M = map(int, input().split())
rows = [input() for _ in range(N)]
K = int(input())

print(rows)
for row in sorted(rows, key=lambda row: int(row.split()[K])):
    print(row.split()[K])
    print(row)

# Bài toán sắp xếp các dòng theo thông tin của cột thứ  K nhập vào #
# 1. Nhập dữ liệu vào N,M list,K
# 2. Sử dụng Sorted theo key = stt cot để xắp xếp dữ liệu theo cột đó rồi duyệt và hiển thị từng dòng
