import matplotlib.pyplot as plt

# List of colors
colors = ['#3896C4', '#A0D4EE', '#EA8783', '#FEB5A2', '#BA7E45', '#39B87F']

# Plotting the colors
fig, ax = plt.subplots(1, len(colors), figsize=(12, 2))

for idx, color in enumerate(colors):
    ax[idx].imshow([[color]])
    ax[idx].axis('off')  # Hide the axis

plt.show()
