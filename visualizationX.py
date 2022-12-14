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
    plt.figure(figsize=(40, 2))
    plt.xlabel('i')
    plt.ylabel('x[i]')
    x = []
    y = []

    i = 0
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
        x.append(i)
        y.append(x_i)
        i+=1

    plt.plot(x, y, label='unsorted')
    step = 1
    every = min
    printDistribution(distribution_of_x, every, step)

    # calculating sum:
    res = 0
    i = 0
    x = []
    y = []
    for v in range(min, max):
        if v in distribution_of_x:
            for _ in range(distribution_of_x[v]):
                x.append(i)
                y.append(v)
                res += (i + 1) * v
                i += 1

    plt.plot(x, y, label='sorted')
    plt.legend()
    plt.show()


    return res


def printDistribution(distribution_of_x, every, step):
    for key in distribution_of_x:
        if key == every:
            print(f'{key}:\t {distribution_of_x[key]}')
            every += step


if __name__ == '__main__':
    N, M, q0 = [500, 2, 7]
    t = time()
    print(analyze_trimpazation(N, M, q0))
    if estimate_execution_time:
        print(f'Execution time = {time() - t:.8f} seconds')

