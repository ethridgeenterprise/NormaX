import numpy as np

def normax(x, mu=0, sigma=1, alpha=0, x0=0, beta=0, gamma=0.3):
    normal = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(- (x - mu)**2 / (2 * sigma**2))
    incentive = alpha * (x - x0)
    irrationality = beta * np.tanh(gamma * (x - mu))
    return normal + incentive + irrationality
