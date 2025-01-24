# This code was generated with the help of ChatGPT

import numpy as np
import matplotlib.pyplot as plt

# Define the focal lengths and sensor width
focal_lengths = np.linspace(10, 200, 500)  # Focal lengths from 10mm to 200mm
sensor_width1 = 36  # Standard full-frame sensor width in mm
sensor_width2 = 56
# Calculate field of view (FOV)
def calculate_fov(focal_length, sensor_width):
    return 2 * np.arctan(sensor_width / (2 * focal_length)) * (180 / np.pi)  # Convert radians to degrees

fov_values1 = calculate_fov(focal_lengths, sensor_width1)
fov_values2 = calculate_fov(focal_lengths, sensor_width2)

# Plot the FOV as a function of focal length
plt.figure(figsize=(10, 6))
plt.plot(focal_lengths, fov_values1, label="Theta1: sensor width " +str(sensor_width1)+ "mm")
plt.plot(focal_lengths, fov_values2, label = "Theta2: sensor width " +str(sensor_width2)+ "mm")
plt.title("Camera Field of View vs. Focal Length")
plt.xlabel("Focal Length (mm)")
plt.ylabel("Field of View (degrees)")
plt.grid(True)
plt.legend()
plt.show()
