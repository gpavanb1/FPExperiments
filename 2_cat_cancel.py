import matplotlib.pyplot as plt
from mpmath import mp

# Initialize an empty list to store results
results = []

# Compute exact value
mp.dps = 200
x = mp.mpf(1 + 2**-29)
y = mp.mpf(1 + 2**-30)
exact = x**2 - y**2

# Vary mp.dps from 5 to 60
dps_list = list(range(5, 60))
for dps in dps_list:
    mp.dps = dps  # Set the precision

    x = mp.mpf(1 + 2**-29)
    y = mp.mpf(1 + 2**-30)

    # Evaluate the Gaussian integral
    result = x**2 - y**2

    # Calculate the difference between pi and the Gaussian integral
    error = mp.log10(mp.fabs(exact - result))

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
