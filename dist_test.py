#!/usr/bin/python3

# from collections import OrderedDict as odict
import os
import pickle
from bisect import bisect_left

bit_widths = {'z':1,'j':1,'q':1,'x':1,'k':1,'v':1,'b':1,'p':1,'g':1,'w':1,'y':1,'f':1,'m':2,'c':2,'u':2,'l':3,'d':3,'h':4,'r':4,'s':4,'n':4,'i':4,'o':4,'a':4,'t':5,'e':7}

width_masks = {}
width_depth = 1
for i in range(65):
    width_depth += 1
    width_masks

def hash(word):
    counts = {c:0 for c in bit_widths}
    for c in word:
        counts[c.lower()] = counts.get(c.lower(), 0) + 1

    result = 0
    depth = 0
    for c,width in reversed(bit_widths.items()):
        count = counts[c]
        # how to calculate a bit mask in python efficiently without the -1 hack
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

PICKLE_PATH = os.path.join(os.getcwd(), '.wordcache')

def join_iter(iterable, delimiter):
    """aka intersperse"""
    it = iter(iterable)
    yield next(it)
    for x in it:
        yield delimiter
        yield x

if __name__ == '__main__':
    if os.path.exists(PICKLE_PATH):
        with open(PICKLE_PATH, 'rb') as pickle_file:
            from_word, from_hash, sorted_hashes = pickle.loads(pickle_file.read())
    else:
        from_word, from_hash = hash_all_words()
        sorted_hashes = list(sorted(from_hash))
        with open(PICKLE_PATH, 'xb') as pickle_file:
            pickle_file.write(pickle.dumps((from_word, from_hash, sorted_hashes)))

    while True:
        try:
            word = input("enter a word> ")
            if word in from_word:
                index = bisect_left(sorted_hashes, from_word[word], 0, len(sorted_hashes))
                collisions = from_hash[from_word[word]]
                print("matches for that one word:", *(k for k,_ in zip(join_iter(collisions, ';'), range(10))), f"; and {len(collisions) - 10} more..." if len(collisions) > 10 else "" )
                print("hash for that word:", from_word[word])
            else:
                print("word was not in the corpus")
        except KeyboardInterrupt:
            print('interrupt, exiting')
            break

