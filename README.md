# Bifurcation Diagram of the Logistic Map

## Overview
This project generates a bifurcation diagram of the logistic map, a classic example of how simple nonlinear dynamical systems can exhibit chaotic behavior. The logistic equation used is:

\[ x_{n+1} = r \cdot x_n \cdot (1 - x_n) \]

where:
- \( r \) is the growth rate parameter,
- \( x_n \) represents population proportion (or any variable in the range \( 0 < x < 1 \)),
- \( n \) is the iteration number.

The diagram visualizes how the steady-state values of \( x \) change as \( r \) increases.

## Features
- **Fixed parameter values for optimal visualization:** The chosen values ensure the best representation of chaotic behavior.
- **Adjustable growth rate (r) range:** The diagram explores \( r \) values from **2.5 to 4.0**, capturing the transition from stability to chaos.
- **High-resolution plotting:** Uses `dpi=300` for better clarity.
- **Grid and tick control:** Custom major and minor ticks improve readability.
- **Efficient computation:** Only the last 100 iterations of each \( r \) value are plotted to focus on attractor behavior.

## Why These Parameter Values?
The selected values of `r_values`, `n`, and `last_n` are chosen to highlight the key features of the logistic map:
- **Growth rate range (2.5 to 4.0):** This range captures the transition from stable fixed points to periodic bifurcations and eventually chaotic behavior. Lower values of \( r \) lead to stable equilibrium, while higher values lead to chaos.
- **Iteration count (`n = 1000`):** The system needs sufficient iterations to settle into its long-term behavior. Too few iterations may not allow transient effects to dissipate.
- **Last 100 iterations (`last_n = 100`):** Instead of plotting every iteration, we only display the final 100 iterations to focus on the attractors of the system. This reduces noise and enhances clarity.

## Requirements
Ensure you have the following dependencies installed:
```sh
pip install matplotlib numpy
```

## Usage
Run the script with Python:
```sh
python bifurcation_diagram.py
```

## Explanation of Key Components
- **Iteration Process:** The script iterates through different \( r \) values and computes the logistic equation.
- **Visualization:** The last few iterations of each \( r \) value are plotted to reveal periodicity and chaos.
- **Grid Customization:** Major ticks are defined at intervals of 0.1 for better clarity.
- **Optimization:** Only the last 100 values per \( r \) are plotted to reduce clutter while preserving key behaviors.

## Example Output
The generated bifurcation diagram showcases stable points, period-doubling bifurcations, and chaotic regions as \( r \) increases.

## Future Improvements
- Increase resolution by sampling more \( r \) values.
- Allow user input to define range and iteration parameters.
- Implement color-coded visualization for better contrast in dense regions.

## License
This project is released under the MIT License.

