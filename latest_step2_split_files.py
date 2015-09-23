# -*- coding: utf-8 -*-
"""
Created on Tue Aug 04 22:33:26 2015

@author: Subu Ganesh
"""

file_opener = open('pn_document.txt')
count = 0
for line in file_opener:
    line = line.strip()
    count = count + 1

lines_per_file = count/10

splitLen = lines_per_file         # 20 lines per file
outputBase = 'pn' # output.1.txt, output.2.txt, etc.

# This is shorthand and not friendly with memory
# on very large files (Sean Cavanagh), but it works.
input = open('np_document.txt', 'r').read().split('\n')
print range(0,len(input))
print range(0, len(input), splitLen)
at = 1
for lines in range(0, len(input), splitLen):
    # First, get the list slice
    outputData = input[lines:lines+splitLen]

    # Now open the output file, join the new slice with newlines
    # and write it out. Then close the file.
    output = open(outputBase + str(at) + '.txt', 'w')
    output.write('\n'.join(outputData))
    output.close()

    # Increment the counter
    at += 1