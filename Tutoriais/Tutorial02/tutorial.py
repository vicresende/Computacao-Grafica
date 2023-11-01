from PIL import Image
from color import colorir
from vec3 import Vec3

def generate_ppm_image(filename, width, height):
    with open(filename, 'w') as file:
        file.write(f'P3\n{width} {height}\n255\n')

        for j in range(height):
            for i in range(width):
                pixel_color = Vec3(i / (width - 1), j / (height - 1), 0)
                color_str = colorir(pixel_color)
                file.write(color_str)
                print(color_str, end="")

def ppm_to_png(ppm_filename, png_filename):
    ppm_image = Image.open(ppm_filename)
    ppm_image.save(png_filename, 'PNG')


###
width = 256
height = 256
ppm_filename = 'output.ppm'
png_filename = 'output.png'

generate_ppm_image(ppm_filename, width, height)
ppm_to_png(ppm_filename, png_filename)
