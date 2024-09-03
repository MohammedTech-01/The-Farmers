import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Soil Quality Detector")

# Colors
WHITE = (255, 255, 255)
BROWN = (139, 69, 19)  # Healthy soil
DARK_BROWN = (101, 67, 33)  # Diseased soil
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (169, 169, 169)
GRID_COLOR = (200, 200, 200)  # Light gray for grid lines

# Grid settings
grid_size = 10
cell_size = width // grid_size

# Soil states (True for healthy soil, False for diseased soil)
soil_states = [[True for _ in range(5)] for _ in range(5)]
healing_timers = [[None for _ in range(5)] for _ in range(5)]  # Timer for healing each soil square

# Car position in pixels (start at the center of the first grid square)
car_pos = [cell_size * 2 + cell_size // 2, cell_size * 2 + cell_size // 2]
car_speed = 2.0  # Increase speed
car_lap_complete = False  # Track if the car has completed a lap

# Timers
last_change_time = time.time()
last_move_time = time.time()
last_disease_time = time.time()  # Timer for introducing new diseases
change_interval = 20  # seconds for affecting neighboring soil squares
move_interval = 0.005  # faster interval for smoother movement
heal_delay = 5  # seconds delay before healing
disease_interval = 7  # seconds interval for new disease
pause_duration = 5  # seconds to pause after completing a full lap

# List to track all active diseased soil squares
active_diseased_soil = []

# Function to randomly introduce a new disease
def introduce_disease():
    r, c = random.randint(0, 4), random.randint(0, 4)
    if soil_states[r][c]:  # Only infect if the soil is healthy
        soil_states[r][c] = False
        active_diseased_soil.append([r, c])  # Add to the list of diseased soil squares

# Function to affect neighboring soil squares

# Function to move the car
def move_car():
    global car_pos, car_lap_complete, last_move_time, pause_duration

    car_pos[0] += car_speed  # Move horizontally by half a pixel
    if car_pos[0] >= cell_size * 7 + cell_size // 2:  # If reached the end of the row
        car_pos[0] = cell_size * 2 + cell_size // 2  # Reset to the start of the row
        car_pos[1] += cell_size  # Move down one row

        if car_pos[1] >= cell_size * 7 + cell_size // 2:  # If reached the end of the grid
            car_pos[1] = cell_size * 2 + cell_size // 2  # Reset to the start of the grid
            car_lap_complete = True  # Mark the lap as complete
            last_move_time = time.time()  # Update last move time to include pause

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = time.time()



    # Check if it's time to introduce a new disease
    if current_time - last_disease_time >= disease_interval:
        introduce_disease()
        last_disease_time = current_time

    # Check if the car should move (only if not paused)
    if not car_lap_complete or (car_lap_complete and current_time - last_move_time >= pause_duration):
        if current_time - last_move_time >= move_interval:
            move_car()
            last_move_time = current_time
            if car_lap_complete:
                car_lap_complete = False  # Reset lap completion after the pause

    # Check if the car is on a diseased soil square
    grid_x = int((car_pos[0] - (cell_size * 2 + cell_size // 2)) // cell_size)
    grid_y = int((car_pos[1] - (cell_size * 2 + cell_size // 2)) // cell_size)
    if 0 <= grid_x < 5 and 0 <= grid_y < 5 and soil_states[grid_y][grid_x] is False:
        if healing_timers[grid_y][grid_x] is None:  # If no healing timer is set
            print(f"Alert: Diseased soil detected at Row {grid_y + 1}, Column {grid_x + 1}")
            healing_timers[grid_y][grid_x] = current_time  # Set the healing timer

    # Check if any soil should be healed
    for row in range(5):
        for col in range(5):
            if healing_timers[row][col] is not None and current_time - healing_timers[row][col] >= heal_delay:
                soil_states[row][col] = True  # Heal the soil
                healing_timers[row][col] = None  # Reset the healing timer
                print(f"The soil at Row {row + 1}, Column {col + 1} has been healed!")

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the grid and soil squares
    for row in range(grid_size):
        for col in range(grid_size):
            x = col * cell_size
            y = row * cell_size

            # Determine the color of the soil square
            if 2 <= row < 7 and 2 <= col < 7:
                if soil_states[row - 2][col - 2]:
                    color = BROWN  # Healthy soil
                else:
                    color = DARK_BROWN  # Diseased soil
                pygame.draw.rect(screen, color, (x, y, cell_size, cell_size))
                # Draw grid lines around the square
                pygame.draw.rect(screen, GRID_COLOR, (x, y, cell_size, cell_size), 1)

    # Draw the car as a simple car shape
    car_x = int(car_pos[0])
    car_y = int(car_pos[1])
    pygame.draw.rect(screen, RED, (car_x - cell_size // 4, car_y - cell_size // 6, cell_size // 2, cell_size // 3))  # Car body
    pygame.draw.circle(screen, BLACK, (car_x - cell_size // 6, car_y + cell_size // 6), cell_size // 8)  # Left wheel
    pygame.draw.circle(screen, BLACK, (car_x + cell_size // 6, car_y + cell_size // 6), cell_size // 8)  # Right wheel

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(120)  # Increase the frame rate for smoother movement

# Quit Pygame
pygame.quit()
sys.exit()