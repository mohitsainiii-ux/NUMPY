# # Write a NumPy program using the following dataset:
# Find all positions/indexes containing NaN.
# Count the total number of NaN values.
# Calculate the mean using np.mean().
# Calculate the mean while ignoring NaN.
# Replace every NaN with 0.
# Create a new array where every NaN is replaced with the mean of the non-NaN values.
# Find the maximum value while ignoring NaN.
# Find the minimum value while ignoring NaN.

import numpy as np

data = np.array([
    10, 20, np.nan, 40, 50,
    np.nan, 70, 80, np.nan, 100
])

# 1. Find positions/indexes containing NaN
nan_positions = np.where(np.isnan(data))[0]
print("NaN positions:", nan_positions)


# 2. Count total NaN values
nan_count = np.sum(np.isnan(data))
print("Total NaN values:", nan_count)


# 3. Calculate mean using np.mean()
normal_mean = np.mean(data)
print("Mean using np.mean():", normal_mean)


# 4. Calculate mean while ignoring NaN
mean_without_nan = np.nanmean(data)
print("Mean ignoring NaN:", mean_without_nan)


# 5. Replace every NaN with 0
data_zero = data.copy()
data_zero[np.isnan(data_zero)] = 0

print("NaN replaced with 0:", data_zero)


# 6. Replace NaN with mean of non-NaN values
data_mean = data.copy()
data_mean[np.isnan(data_mean)] = np.nanmean(data_mean)

print("NaN replaced with mean:", data_mean)


# 7. Find maximum while ignoring NaN
maximum = np.nanmax(data)
print("Maximum:", maximum)


# 8. Find minimum while ignoring NaN
minimum = np.nanmin(data)
print("Minimum:", minimum)