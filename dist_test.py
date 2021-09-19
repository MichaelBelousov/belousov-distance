#!/usr/bin/python3

# from collections import OrderedDict as odict
import pickle

bit_widths = {'z':1,'j':1,'q':1,'x':1,'k':1,'v':1,'b':1,'p':1,'g':1,'w':1,'y':1,'f':1,'m':2,'c':2,'u':2,'l':3,'d':3,'h':4,'r':4,'s':4,'n':4,'i':4,'o':4,'a':4,'t':5,'e':7}

def hash(word):
    counts = {c:0 for c in bit_widths}
    for c in word:
        counts[c.lower()] = counts.get(c.lower(), 0) + 1

    result = 0
    depth = 0
    for c,width in reversed(bit_widths.items()):
        count = counts[c]
        result += (count & width) << depth
        depth += width
    return result

def hash_all_words():
    words = {}
    with open('./words_alpha.txt') as word_file:
        words = {word:hash(word) for word in word_file.read().split('\n')}
    reverse = {}
    for k,v in words.items():
        reverse.setdefault(v, []).append(k)
    return words, reverse

import os
import pickle

PICKLE_PATH = os.path.join(os.getcwd(), '.wordcache')

if __name__ == '__main__':
    if os.path.exists(PICKLE_PATH):
        with open(PICKLE_PATH, 'rb') as pickle_file:
            from_word, from_hash, sorted_hashes = pickle.loads(pickle_file.read())
    else:
        from_word, from_hash = hash_all_words()
        sorted_hashes = sorted(from_hash)
        with open(PICKLE_PATH, 'xb') as pickle_file:
            pickle_file.write(pickle.dumps((from_word, from_hash, sorted_hashes)))

    while True:
        try:
            word = input("enter a word:")
        except KeyboardInterrupt:
            break

