# This is a template for problem Sigma-Trimpazation.

from time import time
from collections import defaultdict

# set the following flag to True to estimate execution time
#
# Exact execution time on you device may be different
# from one on Yandex contest platform!
#
# The flag MUST be False when you are submitting your solution!
estimate_execution_time = False

# Fixed parameters of quantum process:
quantum_a = 7 ** 5
quantum_m = 2 ** 31 - 1

performanceMap = {}

def performanceStart(key):
    performanceMap[key] = time()
def performanceEnd(key):
    if estimate_execution_time:
        print(f'{key} took {time() -performanceMap[key]:.6f}')
    del performanceMap[key]
def analyze_trimpazation(n, m, q0):
    '''
    This function generates data with given parameters
    and calculates desired Y value.
    You need to modify it to make it execute faster.
    You can check your progress using estimate_execution_time flag
    at the top of the file.
    '''
    m_div2 = m // 2
    min = -m_div2
    max = m_div2
    q = q0
    if m % 2 == 1:
        max +=1

    # generating x data:

    performanceStart('Init hashmap')
    map = dict.fromkeys((range(min, max)), 0)
    performanceEnd('Init hashmap')

    performanceStart('Filling hashmap')
    for i in range(n):
        # performanceStart('x_i = q % m - m_div2')
        x_i = q % m - m_div2
        # performanceEnd('x_i = q % m - m_div2')
        # performanceStart('q = ((q * quantum_a) % quantum_m)')
        q = ((q * quantum_a) % quantum_m)
        # performanceEnd('q = ((q * quantum_a) % quantum_m)')
        # performanceStart('insert hashmap')
        map[x_i] += 1
        # performanceEnd('insert hashmap')

    step = 1
    every = min
    for key in map:
        if key == every:
            print(f'{key}:\t {map[key]}')
            every += step
    performanceEnd('Filling hashmap')

    performanceStart('Calculating sum')
    # calculating sum:
    res = 0
    i = 0
    for v in range(min, max):
        if v in map:
            for _ in range(map[v]):
                res += (i + 1) * v
                i += 1
    performanceEnd('Calculating sum')
    return res


if __name__ == '__main__':
    N, M, q0 = map(int, input().split())
    t = time()
    print(analyze_trimpazation(N, M, q0))
    if estimate_execution_time:
        print(f'Execution time = {time() - t:.2f} seconds')
