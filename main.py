import pygame

pygame.init()

WIDTH, HEIGHT = 1100, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ozymandias")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

font = pygame.font.Font("assets/fonts/DTM-Mono.otf", 18)


def fade_in_out_text(screen, text, font, color, position, fade_speed=7):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=position)
    for alpha in range(0, 256, fade_speed):
        screen.fill(BLACK)
        text_surface.set_alpha(alpha)
        screen.blit(text_surface, text_rect)
        pygame.display.flip()
        pygame.time.delay(30)
    pygame.time.delay(1000)
    for alpha in range(255, -1, -fade_speed):
        screen.fill(BLACK)
        text_surface.set_alpha(alpha)
        screen.blit(text_surface, text_rect)
        pygame.display.flip()
        pygame.time.delay(30)


def main():
    intro_done = False
    clock = pygame.time.Clock()
    lines = [
        "I met a traveller from an antique land,",
        'Who said - "Two vast and trunkless legs of stone',
        "Stand in the desert.... Near them, on the sand,",
        "Half sunk a shattered visage lies, whose frown,",
        "And wrinkled lip, and sneer of cold command,",
        "Tell that its sculptor well those passions read",
        "Which yet survive, stamped on these lifeless things,",
        "The hand that mocked them, and the heart that fed;",
        "And on the pedestal, these words appear:",
        "My name is Ozymandias, King of Kings;",
        "Look on my Works, ye Mighty, and despair!",
        "Nothing beside remains. Round the decay",
        "Of that colossal Wreck, boundless and bare",
        'The lone and level sands stretch far away."',
    ]

    while not intro_done:
        pygame.event.pump()
        for line in lines:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            fade_in_out_text(screen, line, font, WHITE, (WIDTH // 2, HEIGHT // 2))
        intro_done = True
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
