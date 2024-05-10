import numpy as np
import matplotlib.pyplot as plt

def plot_gradients(gradients, points):
    fig, ax = plt.subplots()

    # Plot gradients
    for grad, point in zip(gradients, points):
        ax.arrow(point[0], point[1], grad[0]/100, grad[1]/100, head_width=0.1, head_length=0.1, fc='blue', ec='blue')
    
        # Calculate perpendicular line
        x = np.linspace(-10, 10)
        y = (-grad[1]*x)/grad[0]

        #perp_grad = np.array([-grad[1], grad[0]])  # Perpendicular gradient
        #perp_line = np.vstack((point - 10 * perp_grad, point + 10 * perp_grad))  # Extend the line for visualization
        
        # Plot perpendicular line
        ax.plot(x, y, linestyle='--', color='red')

    ax.set_aspect('equal', adjustable='box')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True)
    plt.show()

# Example usage
gradients = [np.array([300.1943717671469, 325.0187035194021]), np.array([323.98348405788977, 301.9276150517999])]  # Example gradients
points = [np.array([0, 0]), np.array([0, 0])]  # Corresponding points


plot_gradients(gradients, points)


plt.arrow(point[0], point[1], -gradient[1]/70*((-1)**(i+1)), gradient[0]/70*((-1)**(i+1)), color='blue')
