import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Plant Disease Spread Simulation")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Grid settings
grid_size = 10
cell_size = width // grid_size

# Dot states (True for green, False for black)
dot_states = [[True for _ in range(5)] for _ in range(5)]

# Timers
last_change_time = time.time()
change_interval = 10  # seconds

# Randomly generate the first black dot
black_dot_pos = [random.randint(0, 4), random.randint(0, 4)]
dot_states[black_dot_pos[0]][black_dot_pos[1]] = False

# List to track all active black dots
active_black_dots = [black_dot_pos]

# Function to affect neighboring dots
def affect_neighboring_dots():
    new_black_dots = []
    for black_dot in active_black_dots:
        if dot_states[black_dot[0]][black_dot[1]] is False:  # Only spread if still black
            neighbors = [
                (black_dot[0] - 1, black_dot[1]),  # Above
                (black_dot[0] + 1, black_dot[1]),  # Below
                (black_dot[0], black_dot[1] - 1),  # Left
                (black_dot[0], black_dot[1] + 1)   # Right
            ]

            for r, c in neighbors:
                if 0 <= r < 5 and 0 <= c < 5 and dot_states[r][c]:  # Check if within bounds and is green
                    dot_states[r][c] = False
                    new_black_dots.append([r, c])

    active_black_dots.extend(new_black_dots)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = time.time()

    # Check if it's time to change colors and affect neighboring dots
    if current_time - last_change_time >= change_interval:
        affect_neighboring_dots()
        last_change_time = current_time

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the grid and dots
    for row in range(grid_size):
        for col in range(grid_size):
            x = col * cell_size
            y = row * cell_size

            # Draw grid lines
            pygame.draw.rect(screen, (200, 200, 200), (x, y, cell_size, cell_size), 1)

            # Draw dots in the middle 5x5 area
            if 2 <= row < 7 and 2 <= col < 7:
                dot_x = x + cell_size // 2
                dot_y = y + cell_size // 2
                dot_color = GREEN if dot_states[row - 2][col - 2] else BLACK
                pygame.draw.circle(screen, dot_color, (dot_x, dot_y), cell_size // 4)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()