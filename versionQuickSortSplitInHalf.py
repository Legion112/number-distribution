# This is a template for problem Sigma-Trimpazation.

from time import time


# set the following flag to True to estimate execution time
#
# Exact execution time on you device may be different
# from one on Yandex contest platform!
#
# The flag MUST be False when you are submitting your solution!
estimate_execution_time = True

# Fixed parameters of quantum process:
quantum_a = 7 ** 5
quantum_m = 2 ** 31 - 1


def middle(min, max):
    return (min + max) // 2


def insert(element, sortedList, minIndex, maxIndex):
    if (maxIndex - minIndex) == 1:
        if element < sortedList[minIndex]:
            sortedList.insert(minIndex, element)
        elif element > sortedList[maxIndex]:
            sortedList.append(element)
        else:
            sortedList.insert(maxIndex, element)
        return

    middleIndex = middle(minIndex, maxIndex)
    if (element < sortedList[middleIndex]):
        if (minIndex < middleIndex):
            insert(element, sortedList, minIndex, middleIndex)
            return
        sortedList.insert(middleIndex, element)
    else:
        if (maxIndex > middleIndex):
            insert(element, sortedList, middleIndex, maxIndex)
            return
        sortedList.insert(middleIndex + 1, element)


def binaryTreeInsertion(element, sortedList):
    index = len(sortedList)
    if index == 0:  # zero elements
        sortedList.append(element)
        return
    insert(element, sortedList, 0, len(sortedList) - 1)


def analyze_trimpazation(n, m, q0):
    '''
    This function generates data with given parameters
    and calculates desired Y value.
    You need to modify it to make it execute faster.
    You can check your progress using estimate_execution_time flag
    at the top of the file.
    '''
    m_div2 = m // 2
    q = q0

    # generating x data:
    t = time()
    left = []
    right = []
    for i in range(n):
        x_i = q % m - m_div2
        if x_i < 0:
            left.append(x_i)
        else:
            right.append(x_i)
        q = ((q * quantum_a) % quantum_m)
    left.sort()
    right.sort()
    # calculating sum:
    t = time()
    res = 0
    for i, v in enumerate(left + right):
        res += (i + 1) * v
        res = 0
    return res


if __name__ == '__main__':
    N, M, q0 = map(int, input().split())
    t = time()
    print(analyze_trimpazation(N, M, q0))
    if estimate_execution_time:
        print(f'Execution time = {time() - t:.8f} seconds')
