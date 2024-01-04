import pygame

# NOTE Untuk Stop Music ketik CTRL + C secara bersamaan


def mp3_app():

    pygame.init()

    pygame.mixer.music.load("media/utha.mp3")

    pygame.mixer.music.set_volume(0.5)

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.quit()
