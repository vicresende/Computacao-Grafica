class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

def colorir(pixel_color):
    # Retorna o valor traduzido [0, 255] de cada componente de cor como uma string formatada.
    return f"{int(255.999 * pixel_color.x())} {int(255.999 * pixel_color.y())} {int(255.999 * pixel_color.z())}\n"
