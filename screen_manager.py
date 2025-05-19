import pygame
import sys
import time

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

def show_opening_screen(screen):
    title_font = pygame.font.Font(None, 72)
    button_font = pygame.font.Font("assets/fonts/GameOfSquids.ttf", 21)

    # Load background dan logo
    background_image = pygame.image.load("assets/images/welcome2.png")
    logo_image = pygame.image.load("assets/images/logo.png")  # Logo transparan
    logo_image = pygame.transform.smoothscale(logo_image, (200, 200))  # Ukuran logo disesuaikan

    while True:
        screen.blit(background_image, (0, 0))  # Background
        screen.blit(logo_image, (screen.get_width() // 2 - 100, 80))  # Posisi logo di atas

        title_text = title_font.render("  ", False, WHITE)
        play_text = button_font.render("Play", True, WHITE)
        info_text = button_font.render("Info", True, WHITE)
        exit_text = button_font.render("Exit", True, WHITE)

        title_rect = title_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 3 + 40))
        play_rect = play_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 30))
        info_rect = info_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 90))
        exit_rect = exit_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 150))

        screen.blit(title_text, title_rect)
        pygame.draw.rect(screen, WHITE, play_rect.inflate(20, 10), 2)
        pygame.draw.rect(screen, WHITE, info_rect.inflate(20, 10), 2)
        pygame.draw.rect(screen, WHITE, exit_rect.inflate(20, 10), 2)
        screen.blit(play_text, play_rect)
        screen.blit(info_text, info_rect)
        screen.blit(exit_text, exit_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    return
                elif info_rect.collidepoint(event.pos):
                    show_info_screen(screen)
                elif exit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()


def show_info_screen(screen):
    button_font = pygame.font.Font("assets/fonts/GameOfSquids.ttf", 21)
    info_font = pygame.font.Font(None, 16)

    while True:
        screen.fill(WHITE)
        credit_text = button_font.render("Credits", True, BLUE)
        info_text = info_font.render("Game ini dibuat oleh Hafidh Khoerul Fata.", True, BLACK)
        back_text = button_font.render("Back", True, BLACK)

        credit_rect = credit_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 3 - 100 ))
        info_rect = info_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2+900))
        back_rect = back_text.get_rect(center=(screen.get_width() // 2, screen.get_height() - 100))
        credit_image = pygame.image.load("assets/images/credit.png")

        screen.blit(credit_image,(0,0))
        screen.blit(credit_text, credit_rect)
        screen.blit(info_text, info_rect)
        pygame.draw.rect(screen, BLACK, back_rect.inflate(20, 10), 2)
        screen.blit(back_text, back_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(event.pos):
                    return

def game_over_screen(screen):
    game_over_font = pygame.font.Font(None, 72)
    button_font = pygame.font.Font("assets/fonts/GameOfSquids.ttf", 21)
    start_time = time.time()
    play_again_active = True
    max_width = 200  # Lebar tombol "Play Again"
    button_height = 40  # Tinggi tombol seragam

    # Render teks tombol
    game_over_text = game_over_font.render("GAME OVER", True, RED)
    try_again_text = button_font.render("Restart", True, BLACK)
    exit_text = button_font.render("Exit", True, BLACK)

    # Dapatkan rect dari teks tombol
    try_again_text_rect = try_again_text.get_rect()
    exit_text_rect = exit_text.get_rect()

    # Set ukuran rect tombol dengan tinggi seragam
    try_again_button_rect = pygame.Rect(0, 0, try_again_text_rect.width + 20, button_height)
    exit_button_rect = pygame.Rect(0, 0, exit_text_rect.width + 20, button_height)
    play_again_button_rect = pygame.Rect(0, 0, max_width, button_height)

    # Hitung total lebar semua tombol dan spasi di antara mereka
    horizontal_spacing = 20  # Spasi antar tombol
    total_width = (try_again_button_rect.width +
                   exit_button_rect.width +
                   play_again_button_rect.width +
                   2 * horizontal_spacing)

    # Hitung posisi X awal untuk menempatkan tombol di tengah secara horizontal
    start_x = (screen.get_width() - total_width) // 2
    button_y = screen.get_height() // 2 + 30  # Posisi Y tombol

    # Set posisi untuk setiap tombol
    try_again_button_rect.topleft = (start_x, button_y)
    exit_button_rect.topleft = (start_x + try_again_button_rect.width + horizontal_spacing, button_y)
    play_again_button_rect.topleft = (exit_button_rect.right + horizontal_spacing, button_y)

    # Set posisi teks agar berada di tengah tombol
    try_again_text_rect.center = try_again_button_rect.center
    exit_text_rect.center = exit_button_rect.center

    # Dapatkan rect dari teks "GAME OVER"
    game_over_rect = game_over_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 3))

    while True:
        screen.fill(WHITE)
        screen.blit(game_over_text, game_over_rect)

        # Menggambar bar hijau di belakang tombol "Play Again" sesuai timer
        elapsed_time = time.time() - start_time
        if elapsed_time <= 10:
            green_width = int(play_again_button_rect.width * (1 - elapsed_time / 10))
            if green_width > 0:
                pygame.draw.rect(screen, GREEN, (play_again_button_rect.x, play_again_button_rect.y, green_width, play_again_button_rect.height))
            play_again_button_color = BLACK  # Warna tombol default saat aktif
            play_again_text_color = BLACK  # Warna teks "Play Again" saat aktif
        else:
            play_again_active = False
            play_again_button_color = (169, 169, 169)  # Abu-abu saat waktu habis
            play_again_text_color = (169, 169, 169)  # Teks juga berubah menjadi abu-abu saat waktu habis

        # Render teks tombol "Play Again" dengan warna yang sesuai
        play_again_text = button_font.render("Play Again", True, play_again_text_color)
        play_again_text_rect = play_again_text.get_rect(center=play_again_button_rect.center)

        # Menggambar tombol dan teksnya
        pygame.draw.rect(screen, BLACK, try_again_button_rect, 2)
        pygame.draw.rect(screen, BLACK, exit_button_rect, 2)
        pygame.draw.rect(screen, play_again_button_color, play_again_button_rect, 2)

        screen.blit(try_again_text, try_again_text_rect)
        screen.blit(exit_text, exit_text_rect)
        screen.blit(play_again_text, play_again_text_rect)

        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if try_again_button_rect.collidepoint(event.pos):
                    return "restart"
                elif exit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                elif play_again_active and play_again_button_rect.collidepoint(event.pos):
                    return "play_again"
