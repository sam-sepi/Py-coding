import numpy as np
from scipy.io.wavfile import write
import matplotlib.pyplot as plt


# sampling rate
sampling_rate = 100
# freq
freq = 4 # the number of oscillation
# samples                         
samples = 200

amplitude = 100

# np.arange Return evenly spaced values within a given interval.
# Returns arange : ndarray (n dimensional array)
# Array of evenly spaced values.
x = np.arange(samples)

# sine wave https://en.wikipedia.org/wiki/Sine_wave
y = amplitude * np.sin(2 * np.pi * freq * x / sampling_rate)

# write file
write("example.wav", samples, y)

plt.plot(x, y)
plt.show()