import numpy as np
import matplotlib.pyplot as plt

def refractive_index_bk7(wavelength):
    # Convert wavelength from nm to micrometers
    wavelength_um = wavelength * 1e-3  # Convert from nm to micrometers

    # Sellmeier coefficients for BK7 glass
    A1 = 1.03961212
    B1 = 0.00600069867
    A2 = 0.231792344
    B2 = 0.0200179144
    A3 = 1.01046945
    B3 = 103.560653
    
    # Calculate the refractive index using the Sellmeier equation
    n_squared = (1 
                  + (A1 * wavelength_um2) / (wavelength_um2 - B1) 
                  + (A2 * wavelength_um2) / (wavelength_um2 - B2) 
                  + (A3 * wavelength_um2) / (wavelength_um2 - B3))
    
    n = np.sqrt(n_squared)
    return n

# Example usage
wavelengths = np.linspace(300, 1000, 100)  # Example wavelengths from 300 nm to 1000 nm
refractive_indices = refractive_index_bk7(wavelengths)

# Plotting the results
plt.plot(wavelengths, refractive_indices, label='BK7 Refractive Index')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Refractive Index (n)')
plt.title('Refractive Index of BK7 Glass')
plt.legend()
plt.grid()
plt.show()

