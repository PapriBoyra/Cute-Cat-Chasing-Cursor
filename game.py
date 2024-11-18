import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Cute Cat Chasing Cursor")

# Colors
background_color = (255, 255, 255)  # White
cat_body_color = (200, 160, 200)  # Light pink
eye_color = (0, 0, 0)  # Black
cheek_color = (255, 182, 193)  # Light pink (blush)
smile_color = (0, 0, 0)  # Black

# Cat settings
cat_size = 40  # Radius of the cat's head

# Cat initial position
cat_x, cat_y = screen_width // 2, screen_height // 2
cat_speed = 3

clock = pygame.time.Clock()

# Game loop
while True:
    screen.fill(background_color)  # Clear the screen with the background color
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    # Move the cat towards the cursor
    if cat_x < mouse_x:
        cat_x += cat_speed
    elif cat_x > mouse_x:
        cat_x -= cat_speed

    if cat_y < mouse_y:
        cat_y += cat_speed
    elif cat_y > mouse_y:
        cat_y -= cat_speed

    # Draw the cat's head
    pygame.draw.circle(screen, cat_body_color, (cat_x, cat_y), cat_size)
    
    # Draw the eyes
    eye_radius = 8
    eye_offset_x = 15
    eye_offset_y = 10
    # Left eye
    pygame.draw.circle(screen, eye_color, (cat_x - eye_offset_x, cat_y - eye_offset_y), eye_radius)
    # Right eye
    pygame.draw.circle(screen, eye_color, (cat_x + eye_offset_x, cat_y - eye_offset_y), eye_radius)

    # Add white sparkles in the eyes for cuteness
    sparkle_radius = 3
    pygame.draw.circle(screen, (255, 255, 255), (cat_x - eye_offset_x - 3, cat_y - eye_offset_y - 3), sparkle_radius)
    pygame.draw.circle(screen, (255, 255, 255), (cat_x + eye_offset_x - 3, cat_y - eye_offset_y - 3), sparkle_radius)

    # Draw blush cheeks
    cheek_radius = 6
    cheek_offset_x = 25
    cheek_offset_y = 10
    pygame.draw.circle(screen, cheek_color, (cat_x - cheek_offset_x, cat_y + cheek_offset_y), cheek_radius)
    pygame.draw.circle(screen, cheek_color, (cat_x + cheek_offset_x, cat_y + cheek_offset_y), cheek_radius)

    # Draw the smile
    smile_rect = pygame.Rect(cat_x - 10, cat_y + 5, 20, 10)
    pygame.draw.arc(screen, smile_color, smile_rect, 3.14, 6.28, 2)  # Small semi-circle smile

    # Update the screen
    pygame.display.flip()
    clock.tick(30)  # Limit FPS to 30
