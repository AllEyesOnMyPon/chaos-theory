# Bifurcation Diagram of the Logistic Map

## Overview
This project generates a **bifurcation diagram** of the logistic map, a classic example of how simple nonlinear dynamical systems can exhibit chaotic behavior. The logistic equation used is:

\[ x_{n+1} = r \cdot x_n \cdot (1 - x_n) \]

where:
- \( r \) is the growth rate parameter,
- \( x_n \) represents population proportion (or any variable in the range \( 0 < x < 1 \)),
- \( n \) is the iteration number.

The diagram visualizes how the steady-state values of \( x \) change as \( r \) increases.

## Features
- **Adjustable growth rate (r) range:** The diagram explores \( r \) values from **2.5 to 4.0**.
- **High-resolution plotting:** Uses `dpi=300` for better clarity.
- **Grid and tick control:** Custom major and minor ticks for better readability.
- **Efficient computation:** Only the last **100 iterations** of each \( r \) value are plotted to display attractor behavior.

## Requirements
Ensure you have the following dependencies installed:
```bash
pip install matplotlib numpy
```

## Usage
Run the script with Python:
```bash
python bifurcation_diagram.py
```

## Explanation of Key Components
- **Iteration:** The script iterates through different \( r \) values and computes the logistic equation.
- **Visualization:** The last few iterations of each \( r \) are plotted to reveal periodicity and chaos.
- **Grid Customization:** Major ticks are defined at intervals of **0.1** for clarity.
- **Optimization:** Only the last **100 values** per \( r \) are plotted to reduce clutter.

## Example Output
The generated bifurcation diagram showcases stable points, period-doubling bifurcations, and chaotic regions as \( r \) increases.

## Future Improvements
- Increase resolution by sampling more \( r \) values.
- Allow user input to define range and iteration parameters.
- Implement color-coded visualization for better contrast in dense regions.

## License
This project is released under the MIT License.

