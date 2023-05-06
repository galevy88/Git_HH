import numpy as np
import Globals
import random
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

def crossover(p1, p2, update_vec):
    c1 = p1.deepcopy()
    c2 = p1.deepcopy()
    alpha = [random.choice(update_vec) for _ in range(len(p1.position))]
    for i in range(len(p1.position)):
        c1.position[i] = alpha[i]*p1.position[i] + (1-alpha[i])*p2.position[i]
        c2.position[i] = (1-alpha[i])*p1.position[i] + alpha[i]*p2.position[i]
    return c1, c2

def mutate(x, mu, sigma):
    y = x.deepcopy()
    flag = np.random.rand(*x.position.shape) <= mu
    ind = np.argwhere(flag)
    y.position[ind] += sigma * np.random.randn(*ind.shape) * np.random.randn(*ind.shape)
    return y

def apply_bound(x, varmin, varmax, reset=0.5):
    for i in range(len(x.position) - 1):
        if x.position[i] < varmin:
            x.position[i] = reset
        elif x.position[i] > varmax:
            x.position[i] = reset


def roulette_wheel_selection(p):
    c = np.cumsum(p)
    r = sum(p)*np.random.rand()
    ind = np.argwhere(r <= c)
    return ind[0][0]

def print_top_5(bestsol, pop, it):
        print(f"First Solution : {[x*y for x, y in zip(pop[0].position, Globals.tranformation_vector)]}")
        print(f"Second Solution : {[x*y for x, y in zip(pop[1].position, Globals.tranformation_vector)]}")
        print(f"Third Solution : {[x*y for x, y in zip(pop[2].position, Globals.tranformation_vector)]}")
        print(f"Fourth Solution : {[x*y for x, y in zip(pop[3].position, Globals.tranformation_vector)]}")
        print(f"Fifth Solution : {[x*y for x, y in zip(pop[4].position, Globals.tranformation_vector)]}")
        print("Iteration {}: First  Cost = {}".format(it, bestsol.cost))
        print("Iteration {}: Second Cost = {}".format(it, pop[1].cost))
        print("Iteration {}: Third  Cost = {}".format(it, pop[2].cost))
        print("Iteration {}: Fourth Cost = {}".format(it, pop[3].cost))
        print("Iteration {}: Fifth  Cost = {}".format(it, pop[4].cost))
        
def get_top_5(bestsol, pop):
    top_5 = [bestsol] + pop[1:5]
    return [sol.position for sol in top_5], [sol.cost for sol in top_5]

def apply_parmas_optimization_preferences(x, preferences):
    for i, (key, optimize) in enumerate(preferences.items()):
        if not optimize:
            x.position[i] = getattr(Globals, key.upper())