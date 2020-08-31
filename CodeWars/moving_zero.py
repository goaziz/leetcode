def move_zeros(array):
    index = 0
    for i in range(len(array)):
        if array[i] != 0:
            array[index] = array[i]
            index += 1
    for i in range(index, len(array)):
        array[i] = 0

    return array

