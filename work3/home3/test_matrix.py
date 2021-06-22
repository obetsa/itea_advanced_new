import pytest

from work3.home3.home3_2 import Matrix

@pytest.mark.parametrize(
    "first_matrix, second_matrix, result_matrix", [
        (
            [[2, 2, 2],
             [2, 2, 2],
             [2, 2, 2]],
            [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]],
            [[3, 3, 3],
             [3, 3, 3],
             [3, 3, 3]],
        ),

        (
            [[2, 2],
             [2, 2]],
            [[1, 1],
             [1, 1],],
            [[3, 3],
             [3, 3]],
        ),
    ])

def matrix_add(first_matrix, second_matrix, result_matrix):
    res_matrix = Matrix(first_matrix) + Matrix(second_matrix)
    assert res_matrix == Matrix(result_matrix)


@pytest.mark.parametrize(
    "first_matrix, second_matrix, result_matrix", 
    [(
            [[2, 2, 2],
             [2, 2, 2],
             [2, 2, 2]],
            [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]],
            [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]],
        ),
    ])

def matrix_sub(first_matrix, second_matrix, result_matrix):
    res_matrix = Matrix(first_matrix) - Matrix(second_matrix)
    assert res_matrix == Matrix(result_matrix)