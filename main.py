import pygame
import sys
from game import Game
from assets_manager import load_assets

# Inisialisasi pygame dan layar
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Math Snake RPG")

# Load assets sekali di awal
assets = load_assets()

def main():
    game = Game(screen, WIDTH, HEIGHT, assets)  # Berikan assets ke Game
    game.show_opening_screen()
    while True:
        game.run_game_loop()

if __name__ == "__main__":
    main()
