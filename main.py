import pygame
import sys
import math

from province import Province

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hexagon Grid")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define hexagon size and spacing
HEX_SIZE = 30  # adjust as needed
HEX_SPACING = 2  # adjust as needed

provinces = {}

def draw_hexagon(x, y):
    """Draw a hexagon at the given position."""
    points = []
    for i in range(6):
        angle_deg = 60 * i
        angle_rad = angle_deg * (math.pi / 180)
        points.append((x + HEX_SIZE * math.cos(angle_rad),
                       y + HEX_SIZE * math.sin(angle_rad)))
    pygame.draw.polygon(screen, BLACK, points, HEX_SPACING)

def draw_hexagon_grid(rows, cols):
    """Draw a grid of hexagons."""
    for row in range(rows):
        for col in range(cols):
            # Calculate position of hexagon center
            x = col * HEX_SIZE * 1.5
            y = row * HEX_SIZE * math.sqrt(3) + (col % 2) * HEX_SIZE * math.sqrt(3) / 2
            draw_hexagon(x, y)

    provinces[(row, col)] = Province(population=1000, gold=100)  # Example population and gold values


def display_province_info(province, x, y):
    font = pygame.font.Font(None, 24)
    population_text = font.render(f"Population: {province.population}", True, BLACK)
    gold_text = font.render(f"Gold: {province.gold}", True, BLACK)
    screen.blit(population_text, (x, y))
    screen.blit(gold_text, (x, y + 30))

# Main loop
def main():
    running = True
    selected_province = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    # Check if mouse click is within a hexagon
                    mouse_pos = pygame.mouse.get_pos()
                    for pos, province in provinces.items():
                        x = pos[1] * HEX_SIZE * 1.5
                        y = pos[0] * HEX_SIZE * math.sqrt(3) + (pos[1] % 2) * HEX_SIZE * math.sqrt(3) / 2
                        if math.dist(mouse_pos, (x, y)) < HEX_SIZE:
                            selected_province = province
                            break

        # Fill the background with white
        screen.fill(WHITE)

        # Draw the hexagon grid
        draw_hexagon_grid(9, 16)  # Adjust the number of rows and columns as needed

        # Display selected province info
        if selected_province:
            display_province_info(selected_province, WIDTH - 200, 50)

        # Update the display
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()