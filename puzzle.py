"Project puzzle"

def main_check(lst):
    """Check each row if there any mutual numbers

    Args:
        lst (list(list(int or str))): the board of the game but in another format

    Returns:
        Bool: checks condition
    >>> main_check([['*', '*', '*', '*', ' ', '*', '*', '*', '*'], \
     ['*', '*', '*', '1', ' ', '*', '*', '*', '*'], \
     ['*', '*', '3', ' ', '3', '*', '*', '*', '*'], \
     ['*', ' ', '4', ' ', '1', '*', '*', '*', '*'], \
     [' ', ' ', ' ', ' ', ' ', '9', ' ', '5', ' '], \
     [' ', '6', ' ', ' ', '8', '3', ' ', ' ', '*'], \
     ['3', ' ', ' ', ' ', '1', ' ', ' ', '*', '*'], \
     [' ', ' ', '8', ' ', ' ', '2', '*', '*', '*'], \
     [' ', ' ', '2', ' ', ' ', '*', '*', '*', '*']])
    False
    """
    for element in lst:
        element = [x for x in element if x.isnumeric()]
        if len(element)!=len(set(element)):
            return False
    return True

def column_check(column):
    """Switching rows and lines

    Args:
        number_list (list(list(int or str))): the board of the game but in another format

    Returns:
        (list(list(int or str))): the board of the game but changed rows and lines
    >>> column_check([['*', '*', '*', '*', ' ', '*', '*', '*', '*'], \
    ['*', '*', '*', '1', ' ', '*', '*', '*', '*']])
    [['*', '*'], ['*', '*'], ['*', '*'], ['*', '1'], [' ', ' '], \
['*', '*'], ['*', '*'], ['*', '*'], ['*', '*']]
    """
    res = []
    list_res = []
    for i in range(len(column[0])):
        for elem in column:
            list_res.append(elem[i])
        res.append(list_res)
        list_res = []
    return res


def valid_solution(board):
    """Main function that checks all of the rules

    Args:
        board (list(str)): the board of the game

    Returns:
        Bool: returns bool information about the game rools
    >>> valid_solution(["**** ****","***1 ****","**  3****","* 4 1****",\
    "     9 5 "," 6  83  *","3   1  **","  8  2***","  2  ****"])
    False
    >>> valid_solution(["**** ****","***1 ****","**  3****","* 4  ****",\
    "     9 5 "," 6  8   *","3   1  **","  8  2***","  2  ****"])
    True
    >>> valid_solution(["**** ****","***1 ****","**  3****","* 4  ****",\
    "     9 5 "," 6  8   *","3   1  **","  8  2***","  2  ****"])
    True
    >>> valid_solution(["1*** ****","***1 ****","**  3****","* 4  ****",\
    "     9 5 "," 6  8   *","3   1  **","  8  2***","  2  ****"])
    False
    """
    for number,element in enumerate(board):
        board[number]=[*element]
    return main_check(board) and main_check(column_check(board)) and main_check(colors(board)) \
    and check_white(board)


def colors(board):
    """Creates a list for each color

    Args:
        board (list(list(int or str))): the board of the game but in another format

    Returns:
        (list(list(int or str))): sorting by colors
    >>> colors([['*', '*', '*', '*', ' ', '*', '*', '*', '*'], \
     ['*', '*', '*', '1', ' ', '*', '*', '*', '*'], \
     ['*', '*', '3', ' ', '3', '*', '*', '*', '*'], \
     ['*', ' ', '4', ' ', '1', '*', '*', '*', '*'], \
     [' ', ' ', ' ', ' ', ' ', '9', ' ', '5', ' '], \
     [' ', '6', ' ', ' ', '8', '3', ' ', ' ', '*'], \
     ['3', ' ', ' ', ' ', '1', ' ', ' ', '*', '*'], \
     [' ', ' ', '8', ' ', ' ', '2', '*', '*', '*'], \
     [' ', ' ', '2', ' ', ' ', '*', '*', '*', '*']])
    [[' ', ' ', '3', ' ', ' ', ' ', '2', ' ', ' '], \
[' ', ' ', '6', ' ', ' ', '8', ' ', ' ', '2'], \
['3', '4', ' ', ' ', ' ', ' ', '1', ' ', ' '], \
['1', ' ', ' ', ' ', ' ', '8', '3', ' ', ' '], \
[' ', ' ', '3', '1', ' ', '9', ' ', '5', ' ']]
    >>> colors([['*', '*', '*', '*', '1', '*', '*', '*', '*'], \
     ['*', '*', '*', '1', '2', '*', '*', '*', '*'], \
     ['*', '*', '1', '2', '3', '*', '*', '*', '*'], \
     ['*', '1', '2', '3', '4', '*', '*', '*', '*'], \
     ['1', '2', '3', '4', '5', '6', '7', '8', '9'], \
     ['2', '3', '4', '5', '6', '7', '8', '9', '*'], \
     ['3', '4', '5', '6', '7', '8', '9', '*', '*'], \
     ['4', '5', '6', '7', '8', '9', '*', '*', '*'], \
     ['5', '6', '7', '8', '9', '*', '*', '*', '*']])
    [['1', '2', '3', '4', '5', '6', '7', '8', '9'], \
['1', '2', '3', '4', '5', '6', '7', '8', '9'], \
['1', '2', '3', '4', '5', '6', '7', '8', '9'], \
['1', '2', '3', '4', '5', '6', '7', '8', '9'], \
['1', '2', '3', '4', '5', '6', '7', '8', '9']]
    """
    res = [[] for x in range(5)]
    swit = column_check(board)
    k = 4
    for i in range(0,5):
        res[i] = swit[i][k:k+5]+board[k-5][i+1:i+5]
        k-=1
    return res

def check_white(board):
    """ Function check all white spaces in board and return True? \
    if all white spaces on their places
    >>> check_white([['*', '*', '*', '*', ' ', '*', '*', '*', '*'], \
     ['*', '*', '*', '1', ' ', '*', '*', '*', '*'], \
     ['*', '*', '3', ' ', '3', '*', '*', '*', '*'], \
     ['*', ' ', '4', ' ', '1', '*', '*', '*', '*'], \
     [' ', ' ', ' ', ' ', ' ', '9', ' ', '5', ' '], \
     [' ', '6', ' ', ' ', '8', '3', ' ', ' ', '*'], \
     ['3', ' ', ' ', ' ', '1', ' ', ' ', '*', '*'], \
     [' ', ' ', '8', ' ', ' ', '2', '*', '*', '*'], \
     [' ', ' ', '2', ' ', ' ', '*', '*', '*', '*']])
    True
    >>> check_white([['1', '*', '*', '*', ' ', '*', '*', '*', '*'], \
     ['*', '*', '*', '1', ' ', '*', '*', '*', '*'], \
     ['*', '*', '3', ' ', '3', '*', '*', '*', '*'], \
     ['*', ' ', '4', ' ', '1', '*', '*', '*', '*'], \
     [' ', ' ', ' ', ' ', ' ', '9', ' ', '5', ' '], \
     [' ', '6', ' ', ' ', '8', '3', ' ', ' ', '*'], \
     ['3', ' ', ' ', ' ', '1', ' ', ' ', '*', '*'], \
     [' ', ' ', '8', ' ', ' ', '2', '*', '*', '*'], \
     [' ', ' ', '2', ' ', ' ', '*', '*', '*', '*']])
    False"""
    return set(board[0][0:4] + board[0][5:9] + board[1][0:3] + board[1][5:9] + board[2][0:2] + \
board[2][5:9] + [board[3][0]] + board[3][5:9] + [board[5][8]] + board[6][7:9] + board[7][6:9] +\
board[8][5:9]) == {'*'}


if __name__=="__main__":
    import doctest
    doctest.testmod()
    