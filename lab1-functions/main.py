import matplotlib.pyplot as plt
import numpy as np

def plot_lines():
  cat = ["bored", "happy", "bored", "bored", "happy", "bored"]
  dog = ["happy", "happy", "happy", "happy", "bored", "bored"]
  activity = ["combing", "drinking", "feezding", "napping", "playing", "washing"]

  xs = [1, 2, 3, 4, 5]
  ys = [0, 0, 2, 2, 3]

  fig, ax = plt.subplots(2)
  print(ax)
  ax[0].plot(xs, ys, label="this is our label")
  ax[0].legend()

  ax[1].plot([2, 4, 6], [1, 1, 10], label="foo")
  ax[1].legend()

  plt.show()


def plot_sinus():
  # Plotting function!
  t = np.arange(0.0, 2.0, 0.01)
  # f(t) = 1 + sin(2 * PI * t)
  s = 23 + np.sin(20 * np.pi * t)

  fig, ax = plt.subplots()
  ax.plot(t, s)
  ax.plot(t, s / 2)
  ax.plot(t, s + 5)

  ax.set(xlabel='time (s)', ylabel='voltage (mV)',
        title='About as simple as it gets, folks')
  ax.grid()
  plt.show()


plot_sinus()