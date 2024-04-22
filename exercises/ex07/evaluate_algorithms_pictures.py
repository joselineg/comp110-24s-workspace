"""Evaluate Algorithms with Analyzing Runtime."""


__author__ = "730662932"


import matplotlib.pyplot as plt
from runtime_analysis_functions import evaluate_runtime


START_SIZE: int = 0
END_SIZE: int = 1000


times = evaluate_runtime("insertion_sort", START_SIZE, END_SIZE)
plt.plot(times)
plt.title("Runtime Analysis of Insertion Sort - joseline")
plt.show()
