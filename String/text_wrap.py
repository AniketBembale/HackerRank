
'''
You are given a string  and width .
Your task is to wrap the string into a paragraph of width .

Function Description

Complete the wrap function in the editor below.

wrap has the following parameters:

->string string: a long string
->int max_width: the width to wrap to

Returns

string: a single string with newline characters ('\n') where the breaks should be
Input Format

The first line contains a string,string .
The second line contains the width, maxwidth.

Constraints
0 < len(string) < 1000
0 < maxwidth < len(string)

Sample Input 0
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
-------------------
Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ'''

#Solution 1

import textwrap

def wrap(string, max_width):
    wrapped_lines = textwrap.wrap(string, max_width)
    return '\n'.join(wrapped_lines)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)




#Solution2 
def wrap(string,max_width):
    return '\n'.join(string[i:i+max_width] for i in range(0,len(string),max_width))


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    