import sys

GRID = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

assert len(GRID) > 1

MAX_I = len(GRID[0]) - 1
MAX_J = len(GRID) - 1


def get_possible_values(j, i, trash):
    """
    Try to get all possible values for input position j,i
    :param j: <int> position of the letter
    :param i: <int> position of the letter
    :param trash: <list of tuples> of already used letters (j,i). Example: [ (0,0), (1,2) ]
    :return: <list of tuples> of possible values
    """
    values = []

    if j + 1 <= MAX_J and (j+1, i) not in trash:
        values.append((j+1, i))

    if j - 1 >= 0 and (j-1, i) not in trash:
        values.append((j-1, i))

    if i + 1 <= MAX_I and (j, i+1) not in trash:
        values.append((j, i+1))

    if i - 1 >= 0 and (j, i-1) not in trash:
        values.append((j, i-1))

    return values


def do_iteration(j, i, current_letter, trash, input_value):
    """

    :param trash: <list of tuples> of already used letters (j,i). Example: [ (0,0), (1,2) ]
    :param current_letter: <int>
    :return:
    """

    if current_letter + 1 == len(input_value):
        do_iteration.res = True
        return

    possible = get_possible_values(j, i, trash)

    if not possible:
        return

    for jj, ii in possible:
        letter = GRID[jj][ii]
        if letter == input_value[current_letter + 1]:
            do_iteration(jj, ii, current_letter + 1, list(trash) + [(jj, ii)], input_value)

    return do_iteration.res


def search_start_positions(grid, first_letter):
    """
    Try to find possible letter positions (j,i) in the grid.
    :param grid:
    :param first_letter: <string>, first_letter
    :return: <list of tuples>, example [(0,0), (1,3)]; return [] if the letter is absent in the current GRID.
    """
    result = []
    for j, line in enumerate(grid):
        for i, letter in enumerate(line):
            if letter == first_letter:
                result.append((j, i))

    return result


def get_result(grid, input_value):
    """
    :param grid: <list of lists>
    :param input_value: <string>, example 'ASDGV'
    :return: <bool>
    """
    for start_j, start_i in search_start_positions(grid, input_value[0]):
        trash = [(start_j, start_i)]
        do_iteration.res = False
        do_iteration(start_j, start_i, 0, trash, input_value)
        if do_iteration.res:
            return True
    return False

if __name__ == '__main__':
    for input in open(sys.argv[1] if len(sys.argv) > 1 else r'input.txt').readlines():
        print get_result(GRID, input.replace('\n', ''))
