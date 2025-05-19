import pygame

def load_assets():
    assets = {}
    assets['background_image'] = pygame.image.load("assets/images/bg.png")
    assets['background_image'] = pygame.transform.scale(assets['background_image'], (800, 600))
    assets['head_image'] = pygame.image.load("assets/images/head.png").convert_alpha()
    assets['body_image'] = pygame.image.load("assets/images/body.png").convert_alpha()
    assets['tail_image'] = pygame.image.load("assets/images/tail.png").convert_alpha()
    assets['head_image'] = pygame.transform.scale(assets['head_image'], (13, 13))
    assets['body_image'] = pygame.transform.scale(assets['body_image'], (13, 13))
    assets['tail_image'] = pygame.transform.scale(assets['tail_image'], (13, 13))
    assets['font'] = pygame.font.Font("assets/fonts/Roboto-Light.ttf", 10)
    assets['hud_font'] = pygame.font.Font("assets/fonts/GameOfSquids.ttf", 21)
    assets['question_font'] = pygame.font.Font("assets/fonts/Roboto-Light.ttf", 50)
    return assets
