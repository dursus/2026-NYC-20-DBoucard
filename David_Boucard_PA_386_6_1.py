# Import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Assign x and y coordinates and set the hex code color of each category
Expenses = ['Groceries', 'Utilities', 'Transportation', 'Dining Out', 'Entertainment']
Amount = [500, 300, 200, 400, 250]
bar_colors = ['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600']

# Plot bar chart (for horizontal bars, use height instead of width)
plt.barh(Expenses, Amount, color=bar_colors, height=0.8)

# Adding labels to the axes
plt.xlabel('Amount Spent ($)')
plt.ylabel('Expense Categories')

# Display the title
plt.title('Monthly Expenses Distribution')

# Show the plot (include tight_layout() to prevent clipping of labels)
plt.tight_layout()
plt.show()