""" This version is not production-like style, it is compact version in 30 lines, just for fun """
from collections import Counter
import sys

cv = lambda i: map(lambda x: int({'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}.get(x, x)), i) # cv -> card values
mc = lambda i: Counter(i).most_common() # mc -> most common

hc = lambda _,__,x: sorted(x, reverse=True) # hc
one_pair = lambda _,__,x: [mc(x)[0][0]] + sorted(x, reverse=True) if len(mc(x)) == 4 and mc(x)[0][1] == 2 else None
two_pairs = lambda _,__,x: sorted([mc(x)[0][0], mc(x)[1][0]], reverse=True) + [mc(x)[2][0]] if len(mc(x)) == 3 and mc(x)[0][1] == 2 else None
three_of_a_kind = lambda _,__,x: [mc(x)[0][0]] + sorted([mc(x)[1][0], mc(x)[2][0]], reverse=True) if len(mc(x)) == 3 and mc(x)[0][1] == 3 else None
straight = lambda _,__,x: hc(_,__,x) if len(set(x)) == 5 and (max(x) - min(x) == 4 or x == [2, 3, 4, 5, 14]) else None
flush = lambda _,x,__: hc(_,x,__) if len(set(x)) == 1 else None
full_house = lambda _,__,x: [mc(x)[0][0], mc(x)[1][0]] if (len(mc(x)) == 2 and mc(x)[0][1] == 3) else None
four_of_a_kind = lambda _,__,x: [mc(x)[0][0],mc(x)[1][0]] if mc(x)[0][1] == 4 else None
straight_flush = lambda x,_,__: hc(x,_,__) if flush(x,_,__) and straight(x,_,__) else None
royal_flush = lambda _,__,x: [1,] if flush(_,__,x) and (x == range(10,15)) else None
all_variants = [royal_flush, straight_flush, four_of_a_kind, full_house, flush, straight, three_of_a_kind, two_pairs, one_pair, hc]

def get_res(variant, hands):
    full_hand = lambda hand: (hand, list(''.join(hand)[1::2]), sorted(cv(list(''.join(hand)[0::2]))))
    l, r = map(lambda x: variant(*full_hand(x)), (hands[:14].split(' '), hands.replace('\n', '')[15:].split(' ')))
    get_res.cache = 'left' if l > r else 'right' if l < r else 'none' if (r and l == r) else None
    return get_res.cache

get_winner = lambda hands: next((get_res.cache for variant in all_variants if get_res(variant, hands)))

for hands in open(sys.argv[1] if len(sys.argv) > 1 else r'input.txt').readlines():
    print get_winner(hands)

#==============================================================================================================================================
# def runTests():
#     tests = [('6D 7H AH 7S QC 6H 2D TD JD AS', 'left'),
#              ('JH 5D 7H TC JS JD JC TS 5S 7S', 'none'),
#              ('2H 8C AD TH 6H QD KD 9H 6S 6C', 'right'),
#              ('JS JH 4H 2C 9H QH KC 9D 4D 3S', 'left'),
#              ('TC 7H KH 4H JC 7D 9S 3H QS 7S', 'right'),
#              ('7D 9S 3H QS 7S TC 7H KH 4H JC', 'left'),
#              ('2C 3H 8H 6H 6C 2C 3H 8H 5H 5C', 'left'),
#              ('2C 6H 6H 4H 4C 2C 6H 6H 5H 5C', 'right'),
#              ('2C 6H 6H 4H 4C 2C 6H 6H 5H 5C', 'right'),
#              ('2C 3H 4H 5H 6C 2C 3H AH 5H 4C', 'right'),
#              ('4C 3H 9H 9H 5C 4C 8H 9H 9H 5C', 'right'),
#              ('TD 3D KD JD AD TD 4D KD JD AD', 'right'),
#              ('TD QD KD JD AD TD QD KD JD AD', 'none'),
#              ('TD QD KD JD AD TD QD KD JD AD', 'none'),
#              ('3D 3D 4D 4D 5D 3D 3D 4D 4D 5D', 'none'),
#              ('3D 3D 4D 4D AD 3D 3D TD 4D 4D', 'left'),
#              ('QD QD AH AD 2D JD JD AH AD KD', 'left'),
#              ('AD JD QD KD TD JD JD AD AD KD', 'left'),
#              ]
#
#     for hands, expect in tests:
#         res = get_winner(hands)
#         assert res == expect, '%s %s %s' % (hands, expect, res)
#         #print 'pass'
#
# runTests()
#==============================================================================================================================================