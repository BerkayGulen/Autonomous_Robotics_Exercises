import numpy as np

# PART A
print("PART A")
std = 2.0
mean = 5.0
vector1 = np.random.normal(loc=mean, scale=std, size=1000000)
print(vector1)
print("************************************")

# PART B
print("PART B")
vector2 = np.random.uniform(0, 10, 1000000)
print(vector2)
print("************************************")


# PART C
print("PART C")

# first vector
std = 2.0
mean = 5.0
vector1 = np.random.normal(loc=mean, scale=std, size=1000000)
first_vector_mean = np.mean(vector1)
first_vector_std = np.std(vector1)
print(first_vector_mean)
print(first_vector_std)

# second vector
std1 = 3.0
mean1 = 4.0
vector2 = np.random.normal(loc=mean1, scale=std1, size=1000000)
second_vector_mean = np.mean(vector2)
second_vector_std = np.std(vector2)
print(second_vector_mean)
print(second_vector_std)
print("************************************")

# The results are the given in the first question is consistent to the result calculated by using mean() and std().

# PART D
print("PART D")
# first vector
std = 2.0
mean = 5.0
vector1=np.random.seed(1) # I added this part
vector1 = np.random.normal(loc=mean, scale=std, size=1000000)
first_vector_mean = np.mean(vector1)
first_vector_std = np.std(vector1)
print(first_vector_mean)
print(first_vector_std)

# second vector
std1 = 3.0
mean1 = 4.0
vector2=np.random.seed(1) # I added this part
vector2 = np.random.normal(loc=mean1, scale=std1, size=1000000)
second_vector_mean = np.mean(vector2)
second_vector_std = np.std(vector2)
print(second_vector_mean)
print(second_vector_std)
print("************************************")

# I added np.random.seed(1) so the distributions are exactly the same each time I started the script