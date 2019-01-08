values = list(range(1, 11)) + 'Jack Queen King'.split()
suits = 'diamonds clubs hearts spades'.split()
deck = ['{} of {}'.format(v, s) for v in values for s in suits]

import copy
total_num = len(copy.deepcopy(deck))

from random import shuffle
shuffle(deck)

while deck:
    if len(deck) == total_num:
        input('Please press ''Enter'' to deal a poker')
        print(deck.pop())
    elif len(deck) == total_num-1:
        input('Keep on')
        print(deck.pop())
    else:
        input()
        print(deck.pop())
print('Finish')
