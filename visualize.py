import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# x = np.linspace(0, 10, 1000)
# y1 = np.sin(2 * np.pi * 5 * x)  # First wave
# y2 = np.sin(2 * np.pi * 4.5 * x)  # Second wave
# y_total = y1 + y2  # Superposition

# plt.plot(x, y_total)
# plt.title("Moiré Pattern from Two Sine Waves")
# plt.show()


def create_moire_3d(frequency1, frequency2, amplitude1=1, amplitude2=1, resolution=100):
    """
    Creates a 3D moiré pattern using sine waves.

    Args:
        frequency1 (tuple): Frequencies (fx, fy) for the first wave.
        frequency2 (tuple): Frequencies (fx, fy) for the second wave.
        amplitude1 (float): Amplitude of the first wave.
        amplitude2 (float): Amplitude of the second wave.
        resolution (int): Number of points along each axis.

    Returns:
        tuple: (X, Y, Z) coordinates of the moiré surface.
    """

    x = np.linspace(-5, 5, resolution)
    y = np.linspace(-5, 5, resolution)
    X, Y = np.meshgrid(x, y)

    Z1 = amplitude1 * np.sin(frequency1[0] * X + frequency1[1] * Y)
    Z2 = amplitude2 * np.sin(frequency2[0] * X + frequency2[1] * Y)

    Z = Z1 + Z2  # Superposition

    return X, Y, Z

# Parameters for the moiré pattern
freq1 = (1, 1.2)  # Frequencies for the first wave
freq2 = (1.1, 1)  # Frequencies for the second wave

# Create the moiré pattern
X, Y, Z = create_moire_3d(freq1, freq2)

# Plot the 3D surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Moiré Pattern')

plt.show()