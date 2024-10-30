import matplotlib.pyplot as plt
import numpy as np

def draw_square(ax, bottom_left, side_length, angle):
    rot_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])

    corners = np.array([
        [0, 0],
        [side_length, 0],
        [side_length, side_length],
        [0, side_length]
    ]).dot(rot_matrix) + bottom_left

    ax.fill(corners[:, 0], corners[:, 1], "b", edgecolor="black")

def draw_pythagoras_tree(ax, bottom_left, side_length, angle, depth):
    """Recursively draws the Pythagoras Tree fractal."""
    if depth == 0:
        return
    
    # Draw current square
    draw_square(ax, bottom_left, side_length, angle)

    # Calculate the new points for the top two squares
    top_left = bottom_left + np.array([0, side_length]).dot([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    top_right = bottom_left + np.array([side_length, side_length]).dot([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])

    # Side length of the child squares
    new_side_length = side_length / np.sqrt(2)
    new_angle_left = angle + np.pi / 4 # Rotate by 45 degree
    new_angle_right = angle - np.pi / 4 # Rotate by -45 degree

    draw_pythagoras_tree(ax, top_left, new_side_length, new_angle_left, depth - 1)
    draw_pythagoras_tree(ax, top_right, new_side_length, new_angle_right, depth - 1)

def main():
    # Initial parameters
    initial_bottom_left = np.array([0, 0])
    initial_side_length = 1
    initial_angle = 0
    depth = 10

    _, ax = plt.subplots()
    ax.set_aspect("equal")
    ax.axis("off")

    draw_pythagoras_tree(ax, initial_bottom_left, initial_side_length, initial_angle, depth)

    plt.show()

if __name__ == '__main__':
    main()