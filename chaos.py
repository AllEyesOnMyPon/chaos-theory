import matplotlib.pyplot as plt # Import the matplotlib library for plotting
# xn+1​\=r⋅xn​⋅(1−xn​)  
# This is a simple implementation of the logistic map in Python.
r = float(input("r = ")) # r is the growth rate parameter for the logistic map
n = int(input("n = ")) # n is the number of iterations to perform
x_value_list = [(0, 0)] * (n + 1)   # Initialize a list to store the x values, with the first element as (0, 0) # The list will store tuples of (iteration, x value)
x_value_list[0] = (0, float(input("x0 = "))) # x0 is the initial value (0 < x0 < 1)

for counter in range(1, n + 1): # Iterate from 1 to n
    xn = r * x_value_list[counter - 1][1] * (1 - x_value_list[counter - 1][1]) # Calculate the next x value using the logistic map formula
    x_value_list[counter] = (counter, xn) # Store the iteration number and the x value in the list

print(x_value_list)




