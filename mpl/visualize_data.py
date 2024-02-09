import matplotlib.pyplot as plt
import numpy as np

# Initialize empty plot
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()
line, = ax.plot([], [])  # Empty line object

# Set up axes
ax.set_xlim(0, 100)  # Adjust as needed
ax.set_ylim(0, 1)    # Adjust as needed
ax.set_xlabel('Time')
ax.set_ylabel('Sensor Value')

# Main loop for updating the plot
while True:
    # Get new data from sensor (replace this with actual data acquisition)
    x = np.arange(100)
    y = np.random.random(100)  # Dummy data
    
    # Update the plot with new data
    line.set_data(x, y)
    
    # Adjust plot limits if necessary
    ax.relim()
    ax.autoscale_view()
    
    # Draw the updated plot
    fig.canvas.draw()
    fig.canvas.flush_events()
    
    # Optional: Pause to control the refresh rate
    plt.pause(0.1)  # Adjust as needed

