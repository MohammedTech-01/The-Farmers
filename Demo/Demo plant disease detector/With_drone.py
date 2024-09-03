import pygame
import sys
import random
import time
import math  # Import the math module for trigonometric functions
import os  # Import os to handle file operations

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Plant Disease Detector")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (169, 169, 169)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Grid settings
grid_size = 9
cell_size = width // grid_size

# Predefined positions for black dots (diseased plants)
predefined_diseases = [(1, 2), (4, 3)]  # Example positions for black dots

# Dot states (True for green, False for black)
dot_states = [[True for _ in range(5)] for _ in range(5)]
healing_timers = [[None for _ in range(5)] for _ in range(5)]  # Timer for healing each plant

# Drone position in pixels
drone_pos = [cell_size * 2, cell_size * 2]  # Start at top-left corner of the 5x5 grid
drone_speed = 2.0  # Increase speed
drone_lap_complete = False  # Track if the drone has completed a lap


# Timers
last_change_time = time.time()
last_move_time = time.time()
last_disease_time = time.time()  # Timer for introducing new diseases
change_interval = 20  # seconds for affecting neighboring dots
move_interval = 0.005  # faster interval for smoother movement
heal_delay = 5  # seconds delay before healing
disease_interval = 14  # seconds interval for new disease
pause_duration = 5  # seconds to pause after completing a full lap

# List to track all active black dots
active_black_dots = []

# Initialize dot states based on predefined diseases
for r, c in predefined_diseases:
    dot_states[r][c] = False
    active_black_dots.append([r, c])  # Add to the list of diseased plants

# Function to randomly introduce a new disease
def introduce_disease():
    r, c = random.randint(0, 4), random.randint(0, 4)
    if dot_states[r][c]:  # Only infect if the plant is healthy
        dot_states[r][c] = False
        active_black_dots.append([r, c])  # Add to the list of diseased plants

# Function to affect neighboring dots
def affect_neighboring_dots():
    new_black_dots = []
    for black_dot in active_black_dots[:]:
        if dot_states[black_dot[0]][black_dot[1]] is False:
            neighbors = [
                (black_dot[0] - 1, black_dot[1]),  # Above
                (black_dot[0] + 1, black_dot[1]),  # Below
                (black_dot[0], black_dot[1] - 1),  # Left
                (black_dot[0], black_dot[1] + 1)   # Right
            ]

            for r, c in neighbors:
                if 0 <= r < 5 and 0 <= c < 5 and dot_states[r][c]:
                    dot_states[r][c] = False
                    new_black_dots.append([r, c])
        else:
            active_black_dots.remove(black_dot)

    active_black_dots.extend(new_black_dots)

# Function to move the drone
def move_drone():
    global drone_pos, drone_lap_complete, last_move_time, pause_duration

    drone_pos[0] += drone_speed  # Move horizontally by half a pixel
    if drone_pos[0] >= cell_size * 7:  # If reached the end of the row
        drone_pos[0] = cell_size * 2  # Reset to the start of the row
        drone_pos[1] += cell_size  # Move down one row

        if drone_pos[1] >= cell_size * 7:  # If reached the end of the grid
            drone_pos[1] = cell_size * 2  # Reset to the start of the grid
            drone_lap_complete = True  # Mark the lap as complete
            last_move_time = time.time()  # Update last move time to include pause

# Function to write alert to file
def write_alert_to_file(message):
    with open('alert.txt', 'w') as file:
        file.write(message)

# Function to delete the alert file
def delete_alert_file():
    if os.path.exists('alert.txt'):
        os.remove('alert.txt')

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

    # Check if it's time to introduce a new disease
    if current_time - last_disease_time >= disease_interval:
        introduce_disease()
        last_disease_time = current_time

    # Check if the drone should move (only if not paused)
    if not drone_lap_complete or (drone_lap_complete and current_time - last_move_time >= pause_duration):
        if current_time - last_move_time >= move_interval:
            move_drone()
            last_move_time = current_time
            if drone_lap_complete:
                drone_lap_complete = False  # Reset lap completion after the pause

    # Check if the drone is on a black dot
    grid_x = int((drone_pos[0] - cell_size * 2) // cell_size)
    grid_y = int((drone_pos[1] - cell_size * 2) // cell_size)
    if 0 <= grid_x < 5 and 0 <= grid_y < 5 and dot_states[grid_y][grid_x] is False:
        if healing_timers[grid_y][grid_x] is None:  # If no healing timer is set
            alert_message = f"Alert: Disease detected at Row {grid_y + 1}, Column {grid_x + 1}"
            print(alert_message)
            write_alert_to_file(alert_message)  # Write the alert to the file
            healing_timers[grid_y][grid_x] = current_time  # Set the healing timer

    # Check if any plant should be healed
    for row in range(5):
        for col in range(5):
            if healing_timers[row][col] is not None and current_time - healing_timers[row][col] >= heal_delay:
                dot_states[row][col] = True  # Heal the plant
                healing_timers[row][col] = None  # Reset the healing timer
                healed_message = f"The plant at Row {row + 1}, Column {col + 1} has been checked!"
                print(healed_message)
                delete_alert_file()  # Delete the alert from the file
                write_alert_to_file(healed_message)  # Write the healed message to the file

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


    # Draw the drone as a more detailed drone shape
    drone_body_radius = cell_size // 4
    propeller_length = cell_size // 2
    propeller_width = cell_size // 10

    # Drone body
    pygame.draw.circle(screen, GRAY, (int(drone_pos[0]), int(drone_pos[1])), drone_body_radius)

    # Propellers
    for angle in [0, 90, 180, 270]:
        prop_x = drone_pos[0] + drone_body_radius * 1.5 * math.cos(math.radians(angle))
        prop_y = drone_pos[1] + drone_body_radius * 1.5 * math.sin(math.radians(angle))
        prop_rect = pygame.Rect(
            prop_x - propeller_length // 2,
            prop_y - propeller_width // 2,
            propeller_length,
            propeller_width
        )
        prop_rect.center = (prop_x, prop_y)
        pygame.draw.rect(screen, BLACK, prop_rect)

    # Center detail
    pygame.draw.circle(screen, BLUE, (int(drone_pos[0]), int(drone_pos[1])), drone_body_radius // 2)

    # Additional drone details (optional)
    pygame.draw.line(screen, YELLOW, (drone_pos[0] - drone_body_radius, drone_pos[1]), (drone_pos[0] + drone_body_radius, drone_pos[1]), 2)
    pygame.draw.line(screen, YELLOW, (drone_pos[0], drone_pos[1] - drone_body_radius), (drone_pos[0], drone_pos[1] + drone_body_radius), 2)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(120)  # Increase the frame rate for smoother movement

# Quit Pygame
pygame.quit()
sys.exit()
