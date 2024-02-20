#import any libraries necessary
import numpy as np

#define a list of Fahrenheit temperatures 
fahrenheit_array = [98.6, 100.0, 77.0, 68.0, 32.0, 212.0, 50.0, 86.0, 95.0, 104.0]

#define the list as a numpy array
fahrenheit_array = np.array(fahrenheit_array)

#convert the Fahrenheit array to Celsius
celsius_array = (fahrenheit_array - 32) * (5/9)

#print the arrays 
print("Fahrenheit:")
for fahrenheit_temp in fahrenheit_array:
    print(round(fahrenheit_temp, 2), end=" ")
print("\nCelsius:")
for celsius_temp in celsius_array:
    print(round(celsius_temp, 2), end=" ")