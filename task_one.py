from typing import List

import matplotlib.pyplot as plt
import numpy as np

# Allow user to input x and y coordinates
x_coords = list(map(float, input("Enter x coordinates separated by spaces: ").split()))
y_coords = list(map(float, input("Enter y coordinates separated by spaces: ").split()))
i = 1
x1_coords = list(map(float, input("Enter x coordinates separated by spaces: ").split()))
y1_coords = list(map(float, input("Enter y coordinates separated by spaces: ").split()))

x2_coords = list(map(float, input("Enter x coordinates separated by spaces: ").split()))
y2_coords: list[float] = list(map(float, input("Enter y coordinates separated by spaces: ").split()))
#i = 1
#while i <= ' ':
   # print(i)
   # i = i + 1

# Convert input lists to NumPy arrays
x_coords = np.array(x_coords)
y_coords = np.array(y_coords)
x1_coords = np.array(x1_coords)
y1_coords = np.array(y2_coords)
# Create the scatterplot
plt.figure(figsize=(8, 6))
plt.scatter(x_coords, y_coords)

# Add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatterplot of User-Input Data")

# Display the plot
plt.show()
