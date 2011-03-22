#!/usr/bin/env python

from hash import BloomFilter, retrieve_first_sentence, retrieve_all_sentences

bf = BloomFilter([1001, 1003, 1005, 1007])
bf.insert_text('the quick brown fox jumped ')
bf.insert_text('jumped over the lazy dog')

print retrieve_first_sentence(bf, 'the quic')
