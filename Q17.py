# Write a NumPy program that generates 1000 random numbers between 1 and 100 and performs:

# Calculate the mean.
# Calculate the median.
# Calculate the standard deviation.
# Find the minimum and maximum.
# Count numbers greater than 50.
# Count numbers between 30 and 70.
# Find the 25th, 50th, and 75th percentiles.
# Sort the generated array in ascending order.
# Find the top 10 largest values.
# Find the bottom 10 smallest values.

import numpy as np

# Generate 1000 random integers between 1 and 100
np.random.seed(42)

data = np.random.randint(1, 101, 1000)

# 1. Mean
mean = np.mean(data)
print("Mean:", mean)

# 2. Median
median = np.median(data)
print("Median:", median)

# 3. Standard deviation
std = np.std(data)
print("Standard deviation:", std)

# 4. Minimum and maximum
minimum = np.min(data)
maximum = np.max(data)

print("Minimum:", minimum)
print("Maximum:", maximum)

# 5. Count numbers greater than 50
count_greater_50 = np.sum(data > 50)
print("Numbers greater than 50:", count_greater_50)

# 6. Count numbers between 30 and 70
count_between = np.sum((data >= 30) & (data <= 70))
print("Numbers between 30 and 70:", count_between)

# 7. Percentiles
percentiles = np.percentile(data, [25, 50, 75])

print("25th percentile:", percentiles[0])
print("50th percentile:", percentiles[1])
print("75th percentile:", percentiles[2])

# 8. Sort array
sorted_data = np.sort(data)
print("Sorted data:", sorted_data)

# 9. Top 10 largest values
top_10 = sorted_data[-10:]
print("Top 10 largest:", top_10)

# 10. Bottom 10 smallest values
bottom_10 = sorted_data[:10]
print("Bottom 10 smallest:", bottom_10)