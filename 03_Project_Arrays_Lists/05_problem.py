# code to reverse a list in place without using reverse function


def reverse_list(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1

    return lst


# shift right/ rotate right by k elements


def rotate_right(lst, k):
    count = 0
    while count < k:
        temp = lst.pop()
        lst.insert(0, temp)
        count += 1
    return lst


def rotate_left(lst, k):
    count = 0
    while count < k:
        temp = lst.pop(0)
        lst.append(temp)
        count += 1
    return lst


# in place remove duplicates
def remove_duplicates_sorted(lst):
    i = 0
    while i < len(lst) - 1:
        if lst[i] == lst[i + 1]:
            lst.pop(i + 1)
        else:
            i += 1
    return lst


def is_palindrome(string):
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


# code to transpose a matrix in place without using .T


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(i + 1, cols):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix


def rotate_matrix_right_90(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(i + 1, cols):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
    return matrix


def rotate_matrix_left_90(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(i + 1, cols):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    matrix.reverse()
    return matrix


def rotate_matrix_right_180(matrix):
    matrix.reverse()
    for row in matrix:
        row.reverse()

    return matrix


def rotate_matrix_left_180(matrix):
    matrix.reverse()
    for row in matrix:
        row.reverse()

    return matrix


def rotate(direction, matrix, angle):
    if direction == "right":
        if angle == 90:
            return rotate_matrix_right_90(matrix)
        elif angle == 180:
            return rotate_matrix_right_180(matrix)
        elif angle == 270:
            return rotate_matrix_left_90(matrix)
    elif direction == "left":
        if angle == 90:
            return rotate_matrix_left_90(matrix)
        elif angle == 180:
            return rotate_matrix_left_180(matrix)
        elif angle == 270:
            return rotate_matrix_right_90(matrix)
    return matrix
