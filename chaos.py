# xn+1​\=r⋅xn​⋅(1−xn​) 

x0 = float(input("x0 = ")) # Initial value
r = float(input("r = ")) # Growth rate
# The logistic map is a polynomial mapping of degree 2. It is used to model population growth.
n = int(input("n = ")) # Number of iterations
# The number of iterations is the number of times the equation will be applied to the initial value.

x_value_list = [x0] # List to store the values of x

counter = 0 # Counter to keep track of the number of iterations

while counter < n: # While the counter is less than the number of iterations
    counter += 1 
    next_value = r * x_value_list[counter - 1] * (1 - x_value_list[counter - 1]) # The logistic map equation
    x_value_list.append(next_value) 

print(x_value_list) 



