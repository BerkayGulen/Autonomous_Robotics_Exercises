import numpy as np
import timeit

# Berkay Gülen -- 20170613017

# EXERCISE 1 PART A
def sample_normal_twelve(mu, sigma):
    # Sample from a normal distribution using 12 uniform samples
    # it returns sample from normal distribution with mean = 0
    return (0.5 * np.random.uniform(-sigma, sigma, 12)).sum() + mu


# ---------------------------------------------------------------------------------------

# EXERCISE 1 PART B
def evaluate_sampling_time(mu, sigma, n_samples, sampling_function):
    tic = timeit.default_timer()

    # using the sample_normal_twelve func and np.random.normal func with reference of sampling_function
    for i in range(n_samples):
        sampling_function(mu, sigma)

    toc = timeit.default_timer()
    time_per_sample = (toc - tic) / n_samples * 1e6
    print("%s : %.3f us" % (sampling_function.__name__, time_per_sample))


evaluate_sampling_time(0, 2, 1000, sample_normal_twelve)
evaluate_sampling_time(0, 2, 1000, np.random.normal)
