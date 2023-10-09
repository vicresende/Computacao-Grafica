"""
    Computação Gráfica
    Atividade 01
    Victória Resende - 759539
"""

from PIL import Image
import numpy as np

class ImageSaver:
    def __init__(self):
        pass

    @staticmethod
    def save_ppm(filename, width, height, pixels):
        with open(filename, 'w') as file:
            file.write(f'P3\n{width} {height}\n255\n')

            for pixel in pixels:
                file.write(f'{pixel[0]} {pixel[1]} {pixel[2]}\n')

    @staticmethod
    def save_png(filename, width, height, pixels):
        img = Image.new('RGB', (width, height))
        img.putdata(pixels)
        img.save(filename, 'PNG')

def generate_gradient(width, height):
    pixels = []
    for j in range(height):
        for i in range(width):
            r = i / (width - 1)
            g = j / (height - 1)
            b = 0

            ir = int(255.999 * r)
            ig = int(255.999 * g)
            ib = int(255.999 * b)

            pixels.append((ir, ig, ib))
    return pixels

def generate_circle(width, height):
    pixels = []
    cx, cy = width // 2, height // 2
    radius = min(cx, cy) * 0.8

    for j in range(height):
        for i in range(width):
            dx = i - cx
            dy = j - cy
            distance = np.sqrt(dx * dx + dy * dy)

            if distance < radius:
                r = 255
                g = 0
                b = 255

            else:
                r = 255
                g = 255
                b = 255

            pixels.append((r, g, b))
    return pixels


def generate_square(width, height):
    pixels = []
    square_size = min(width, height) * 0.6

    for j in range(height):
        for i in range(width):
            x_margin = (width - square_size) // 2
            y_margin = (height - square_size) // 2

            if i >= x_margin and i < x_margin + square_size and j >= y_margin and j < y_margin + square_size:
                r = 200
                g = 160
                b = 255
            else:
                r = 255
                g = 255
                b = 255

            pixels.append((r, g, b))
    return pixels


# Criação das imagens
width = 256
height = 256

saver = ImageSaver()

# Imagem 1: Degradê
print("Gerando imagem degradê...")
pixels = generate_gradient(width, height)
saver.save_ppm('gradient.ppm', width, height, pixels)
saver.save_png('gradient.png', width, height, pixels)

# Imagem 2: Círculo
print("Gerando imagem de círculo...")
pixels = generate_circle(width, height)
saver.save_ppm('circle.ppm', width, height, pixels)
saver.save_png('circle.png', width, height, pixels)

# Imagem 3: Quadrado
print("Gerando imagem de quadrado...")
pixels = generate_square(width, height)
saver.save_ppm('square.ppm', width, height, pixels)
saver.save_png('square.png', width, height, pixels)

print("Geração concluída.")
