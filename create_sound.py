import numpy as np
import wave

t = np.linspace(0, 1, 44100)
data = (np.sin(2 * np.pi * 1000 * t) * 32767).astype(np.int16)

w = wave.open('alert.wav', 'w')
w.setnchannels(1)
w.setsampwidth(2)
w.setframerate(44100)
w.writeframes(data.tobytes())
w.close()

print('alert.wav created!')
