class BaseMatrix:
    def __init__(self, width, height, pixel_size):
        self.WIDTH = width
        self.HEIGHT = height
        self.PIX_SIZE = pixel_size

    def display(self):
        pass

    def set_pixel(self, x, y, color):
        pass

    def fill(self, color):
        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                self.set_pixel(x, y, color)

    def run(self):
        self.display()