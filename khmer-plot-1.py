#!/usr/bin/env python

""" The graph drawn by this script shows a breakoff in a success metric
at a bloom-filter k-mer of around k1=6.  Why?

Conclusion:  The overlap term between the two text pieces is 6 characters
long ('jumped').
"""

from hash import BloomFilter, retrieve_first_sentence, retrieve_all_sentences
from itertools import product

first_sent='the quick brown fox jumped '

_min, _max = 3, 17
krange = range(_min, _max)
score_matrix = [[0 for k1 in krange] for k2 in krange]
ideal = float(len('the quick brown fox jumped over the lazy dog'))
for k1, k2 in product(krange, krange):
    bf = BloomFilter([1001, 1003, 1005, 1007], k=k1)
    bf.insert_text(first_sent)
    bf.insert_text('jumped over the lazy dog')

    print "-"*20
    chunk = first_sent[:k2]
    result = retrieve_first_sentence(bf, chunk)
    print "k1     =", k1
    print "k2     =", k2
    print "chunk  =", chunk
    print "result =", result
    score_matrix[k1-_min][k2-_min] = len(result)/ideal

import matplotlib.cm as cm
import matplotlib.pyplot as plt
plt.imshow(score_matrix, cmap = cm.gray)
plt.xlabel('search term length')
plt.ylabel('bloom filter k-mer')
plt.show()
