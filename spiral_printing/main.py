import sys
from itertools import cycle


def get_spiral_elements(width, height, data):
    """

    :param width: <int>
    :param height: <int>
    :param data: <list> of elements for filling the matrix. (P.S. not only <ints>).
    :return:
    """
    assert len(data) == width * height
    ways = cycle([('j_min', 1, 0), ('i_max', 0, 1), ('j_max', -1, 0), ('i_min', 0, -1)])
    res = []

    matrix = [data[i:i+width] for i in xrange(0, height * width, width)]

    borders = {'i_min': 0, 'j_min': 0, 'i_max': width - 1, 'j_max': height - 1}

    current = {'i': 0, 'j': 0}
    steps = {'i': None, 'j': None}

    border, steps['i'], steps['j'] = ways.next()

    for _ in xrange(width*height):
        way = 'i' if steps['i'] else 'j'

        res.append(matrix[current['j']][current['i']])

        if not borders['%s_min' % way]  <= current[way] + steps[way] <= borders['%s_max' % way]:
            borders[border] += (1 if 'min' in border else -1)
            border, steps['i'], steps['j'] = ways.next()

        current['i'] += steps['i']
        current['j'] += steps['j']

    return res

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as test_cases:
        for case in test_cases:
            if case == '\n':
                continue
            splitted_case = case.split(';')

            height = int(splitted_case[0])
            width = int(splitted_case[1])

            data = splitted_case[2].split()

            print ' '.join(map(str,get_spiral_elements(width, height, data)))



