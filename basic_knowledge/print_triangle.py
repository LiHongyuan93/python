# coding=UTF-8
# python version: Python 3.7.6
# 打印等腰倒三角
# output：
# /usr/local/bin/python3.7 /Users/gymboadmin/python/python/.idea/print_triangle.py
# 请出入行数:10
#  * * * * * * * * * *
#   * * * * * * * * *
#    * * * * * * * *
#     * * * * * * *
#      * * * * * *
#       * * * * *
#        * * * *
#         * * *
#          * *
#           *


row = int(input("请出入行数:"))

for line in range(1,row+1):
    blankNum = line
    startNum = row-line+2
    for blank in range(0,blankNum):
        print(' ', end='')
    for start in range(1,startNum,1):
        print("*",end=' ')
    print("")

