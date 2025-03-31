import matplotlib.pyplot as plt # Import the matplotlib library for plotting
import numpy as np # Import the numpy library for numerical operations

r_values = [x * 0.01 + 2.5 for x in range(0, 150)]  # range of r values
n = 1000  # Number of iterations
last_n = 100  # Number of iterations to display for each r

plt.figure(dpi=300)  # Set the figure resolution to 300 dpi
for r in r_values: # Loop through each r value
    x_value_list = [(0, 0)] * (n + 1) # Initialize a list to store x values
    x_value_list[0] = (0, 0.5)  # Let's start with x0 = 0.5

    for counter in range(1, n + 1): # Loop through the iterations
        xn = r * x_value_list[counter - 1][1] * (1 - x_value_list[counter - 1][1]) # Logistic map equation
        x_value_list[counter] = (counter, xn) # Store the current iteration and x value

    # Only plot the last few iterations for each r value
    for i in range(n - last_n, n): # Loop through the last n iterations
        plt.plot(r, x_value_list[i][1], 'o', color='black', alpha=0.25, markersize=1.25) # Plot the points

major_ticks_x = np.arange(2.5, 4.0, 0.1)  # Range x from 2.5 to 4.0, step 0.1
major_ticks_y = np.arange(0, 1.1, 0.1)    # Range y from 0 to 1.1, step 0.1

# Set the major ticks for x and y axes
plt.xticks(major_ticks_x, fontsize=10) 
plt.yticks(major_ticks_y, fontsize=10)
plt.minorticks_on()  # show minor ticks
plt.grid(which='both', linestyle='--', linewidth=0.5)  # Add grid lines for both major and minor ticks

plt.title("Bifurcation Diagram of the Logistic Map") 
plt.xlabel("r value")
plt.ylabel("x")
plt.show()


