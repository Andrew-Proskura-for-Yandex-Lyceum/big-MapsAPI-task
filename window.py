import argparse
import os

import pygame
import requests

def change_picture(server_address, ll, scale, api_key):
    print('1')
    map_request = f"{server_address}"
    params = {'ll': ll, 'z': scale, 'apikey': api_key}
    response = requests.get(map_request, params=params)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)

    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()

    os.remove(map_file)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('coords')
    parser.add_argument('scale')
    args = parser.parse_args()
    server_address = 'https://static-maps.yandex.ru/v1?'
    api_key = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'
    ll = args.coords
    scale = args.scale
    running = True
    while running:
        for i in pygame.event.get():
            if i == pygame.K_PAGEDOWN:
                scale -= 1
                change_picture(server_address, ll, scale, api_key)
            elif i == pygame.K_PAGEUP:
                scale += 1
                change_picture(server_address, ll, scale, api_key)

if __name__ == '__main__':
    main()
