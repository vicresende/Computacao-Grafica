from PIL import Image

def generate_ppm_image(filename, width, height):
    with open(filename, 'w') as file:
        file.write(f'P3\n{width} {height}\n255\n')

        for j in range(height):
            for i in range(width):
                r = i / (width - 1)
                g = j / (height - 1)
                b = 0

                ir = int(255.999 * r)
                ig = int(255.999 * g)
                ib = int(255.999 * b)

                file.write(f'{ir} {ig} {ib}\n')

def ppm_to_png(ppm_filename, png_filename):
    ppm_image = Image.open(ppm_filename)
    ppm_image.save(png_filename, 'PNG')

# Imagem 1
width = 256
height = 256
ppm_filename = 'output.ppm'
png_filename = 'output.png'

generate_ppm_image(ppm_filename, width, height)
ppm_to_png(ppm_filename, png_filename)
