import matplotlib.pyplot as plt
from mpmath import mp, quad

# Initialize an empty list to store results
results = []

# Define the integrand for the Gaussian integral
def gaussian_function(x):
    return mp.exp(-x**2)

# Vary mp.dps from 5 to 100
dps_list = list(range(5, 101))
for dps in dps_list:
    mp.dps = dps  # Set the precision

    # Evaluate the Gaussian integral
    result = quad(gaussian_function, [-mp.inf, mp.inf])**2

    # Calculate the difference between pi and the Gaussian integral
    error = mp.log10(mp.fabs(mp.pi - result))

    # Append the precision and the corresponding error to the results list
    results.append(error)

# Plot the precision (mp.dps) against the exponent of the error
print(dps_list, results)
plt.plot(dps_list, results, '-bo')
plt.xlabel("mp.dps (Precision)")
plt.ylabel("Logarithm of Error")
plt.title("Logarithm of Error vs. Precision")
plt.grid()
plt.show()
