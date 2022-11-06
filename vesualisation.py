import matplotlib.pyplot as plt
from time import time




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

def drawDistribution(map, min, max):
    # plt.xlabel('value')
    # plt.ylabel('number')

    # plt.axis([min, max, 0, M])

    x = [*map.keys()]
    y = [*map.values()]
    print(x)
    print(y)
    plt.plot(x, y, 'ro')
    plt.show()


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

    distribution_of_x = dict.fromkeys((range(min, max)), 0)


    for i in range(n):
        # performanceStart('x_i = q % m - m_div2')
        x_i = q % m - m_div2
        # performanceEnd('x_i = q % m - m_div2')
        # performanceStart('q = ((q * quantum_a) % quantum_m)')
        q = ((q * quantum_a) % quantum_m)
        # performanceEnd('q = ((q * quantum_a) % quantum_m)')
        # performanceStart('insert hashmap')
        distribution_of_x[x_i] += 1
        # performanceEnd('insert hashmap')

    step = 1
    every = min
    for key in distribution_of_x:
        if key == every:
            print(f'{key}:\t {distribution_of_x[key]}')
            every += step

    # calculating sum:
    res = 0
    i = 0
    for v in range(min, max):
        if v in distribution_of_x:
            for _ in range(distribution_of_x[v]):
                res += (i + 1) * v
                i += 1


    drawDistribution(distribution_of_x, min, max)



    return res


if __name__ == '__main__':
    N, M, q0 = [10000000, 5, 1]
    t = time()
    print(analyze_trimpazation(N, M, q0))
    if estimate_execution_time:
        print(f'Execution time = {time() - t:.8f} seconds')

