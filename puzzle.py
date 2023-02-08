def main_check(array):
    pass

def row_check(row):
    pass

def column_check(column):
    '''
    ([['*', '*', '*', '*', ' ', '*', '*', '*', '*'], \
     ['*', '*', '*', '1', ' ', '*', '*', '*', '*'], \
     ['*', '*', '3', ' ', '3', '*', '*', '*', '*'], \
     ['*', ' ', '4', ' ', '1', '*', '*', '*', '*'], \
     [' ', ' ', ' ', ' ', ' ', '9', ' ', '5', ' '], \
     [' ', '6', ' ', ' ', '8', '3', ' ', ' ', '*'], \
     ['3', ' ', ' ', ' ', '1', ' ', ' ', '*', '*'], \
     [' ', ' ', '8', ' ', ' ', '2', '*', '*', '*'], \
     [' ', ' ', '2', ' ', ' ', '*', '*', '*', '*']])
    '''
    res = []
    list_res = []
    for i in range(len(column)):
        for elem in column:
            list_res.append(elem[i])
        res.append(list_res)
        list_res = []
    return res



def colours_check(row):
    pass


def validate_board(board):
    pass