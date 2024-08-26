import matplotlib.pyplot as plt

# Points for line 1
x1 = [1, 2, 3]
y1 = [2, 4, 1]

# Points for line 2
x2 = [1, 2, 3]
y2 = [4, 1, 3]

# Plotting the lines
plt.plot(x1, y1, label='Line 1', marker='o')
plt.plot(x2, y2, label='Line 2', marker='o')

# Adding title and labels
plt.title('Graph of Two Intersecting Lines')
plt.xlabel('X axis')
plt.ylabel('Y axis')

# Adding a legend
plt.legend()

# Display the graph
plt.grid(True)
plt.show()
