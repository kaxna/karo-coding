## place for exercise 1

import matplotlib.pyplot as plt
import numpy as np

# chcemy to: cos(frequency * 2pi * t)

def plot_cosinus():
  t = np.arange(0.0, 2.0, 0.01)
  s = np.cos(5 * 2*np.pi * t)

  fig, ax = plt.subplots()
  ax.plot(t, s, label='base')
  ax.plot(t, s/2 + 2.5, label='s/2 + 2.5')
  ax.plot(t, s*2 - 3.5, label='s*2 - 3.5')

  ax.set(xlabel='t', ylabel='s',
        title='Pierwszy wykres')

  ax.grid()
  ax.legend(loc= 'lower right')
  plt.show()

plot_cosinus()
