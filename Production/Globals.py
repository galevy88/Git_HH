
import numpy as np



CURRENT_CELL = str('combine')



# Varmin Varmax and Gammas

C1 = 0.01
C2 = 55
C3 = 0.1
C4 = 55
C5 = 0.125
C6 = 0.0125
C7 = 65
C8 = 4

easy_varmin = [-100,  -100, -100, -100, -100, -100, -100,  0]
easy_varmax = [ 100,  100,  100, 100,  100,  100, 100, 10]
medium_varmin = [-1,    0, -1,   0, -1, -1,   0,  0]
medium_varmax = [ 1,  100,  1, 100,  1,  1, 100, 10]
extreme_varmin = [0.009, 54.9, 0.09, 54.9,  0.124, 0.0124, 64.9, 0]
extreme_varmax = [0.011,  55.1,  0.11, 55.1, 0.126, 0.0126, 65.1, 10]


easy_gamma = [[-0.001, 0.001], [-0.01, 0.01], [-0.001, 0.001], [-0.01, 0.01], [-0.001, 0.001], [-0.001, 0.001], [-0.01, 0.01], [-0.001, 0.001]]
medium_gamma = [[-0.01, 0.01], [1, 1], [-0.01, 0.01], [1, 1], [-0.01, 0.01], [-0.01, 0.01], [1, 1], [-0.01, 0.01]]
extreme_gamma = [[0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1]]

easy_sigma = np.array([0.1, 2, 0.1, 2, 0.1, 0.1 , 2, 0.1])
medium_sigma = np.array([0.2, 4, 0.2, 4, 0.2, 0.2 , 4, 0.2])
extreme_sigma = np.array([0.3, 6, 0.3, 6, 0.3, 0.3 , 6, 0.3])