from .BaseMatrix import BaseMatrix
import board
import atexit
from neopixel import NeoPixel, GRB

class Matrix(BaseMatrix):
    def __init__(self, width, height, pixel_size):
        super().__init__(width, height, pixel_size)

        PIN = board.D18

        self.pixels = NeoPixel(PIN, width*height, brightness=0.6, auto_write=False, pixel_order=GRB)
        atexit.register(self.__del__)

    def coord_to_pixel(self, x, y):
        pixel = y * self.WIDTH
        pixel += x if y % 2 == 0 else (self.WIDTH-1) - x
        return pixel

    def display(self):
        self.pixels.show()

    def set_pixel(self, x, y, color):
        self.pixels[self.coord_to_pixel(x, y)] = color

    def fill(self, color):
        self.pixels.fill(color)

    def __del__(self):
        self.fill((0,0,0))
        self.run()