import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Set up the dimensions of the grid
width, height = 600, 400
rows, cols = 60, 40
cell_size = width // rows

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create an empty grid
grid = np.zeros((rows, cols), dtype=int)

# Create the Pygame screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Conway's Game of Life")

# Function to update the grid based on mouse input
def update_grid(mouse_pos):
    row, col = mouse_pos[1] // cell_size, mouse_pos[0] // cell_size
    grid[row, col] = 1

# Main game loop
drawing = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            update_grid(pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        elif event.type == pygame.MOUSEMOTION and drawing:
            update_grid(pygame.mouse.get_pos())

    # Create a copy of the grid to store the next generation
    new_grid = np.copy(grid)

    # Update the grid based on the rules of Conway's Game of Life
    for i in range(rows):
        for j in range(cols):
            neighbors_sum = (
                grid[i - 1:i + 2, j - 1:j + 2].sum() - grid[i, j]
            )  # Sum of neighbors excluding the cell itself

            # Apply Conway's rules
            if grid[i, j] == 1 and (neighbors_sum < 2 or neighbors_sum > 3):
                new_grid[i, j] = 0  # Cell dies
            elif grid[i, j] == 0 and neighbors_sum == 3:
                new_grid[i, j] = 1  # Cell becomes alive

    # Update the grid
    grid = np.copy(new_grid)

    # Draw the grid
    screen.fill(BLACK)
    for i in range(rows):
        for j in range(cols):
            color = WHITE if grid[i, j] == 1 else BLACK
            pygame.draw.rect(screen, color, (j * cell_size, i * cell_size, cell_size, cell_size))

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    pygame.time.Clock().tick(10)  # You can adjust the speed by changing the argument
