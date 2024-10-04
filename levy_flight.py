import numpy as np
import math

def levy_flight(Lambda):
    sigma1 = np.power((math.gamma(1 + Lambda) * np.sin((np.pi * Lambda) / 2)) \
                      / math.gamma((1 + Lambda) / 2) * Lambda * np.power(2, (Lambda - 1) / 2), 1 / Lambda)
    sigma2 = 1
    u = np.random.normal(0, sigma1)
    v = np.random.normal(0, sigma2)
    l = u / np.power(np.fabs(v), 1 / Lambda)

    return l    

def m_num(solution_size):
    num = solution_size
    while True:
        l = levy_flight(1.5)
        if np.fabs(l) < num / 2:
            m = int(np.fabs(l)) + 1
        else:
            m = 0

        if m != 0:
            break
    return m

if __name__ == '__main__':
    m()