from datetime import datetime, timedelta
import math

from .BaseApp import BaseApp

num_pix = [
    [
        [1, 1, 1],
        [1, 0, 1],
        [1, 0, 1],
        [1, 0, 1],
        [1, 1, 1]
    ],
    [
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1]
    ],
    [
        [1, 1, 1],
        [0, 0, 1],
        [1, 1, 1],
        [1, 0, 0],
        [1, 1, 1]
    ],
    [
        [1, 1, 1],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 1],
        [1, 1, 1]
    ],
    [
        [1, 0, 1],
        [1, 0, 1],
        [1, 1, 1],
        [0, 0, 1],
        [0, 0, 1]
    ],
    [
        [1, 1, 1],
        [1, 0, 0],
        [1, 1, 1],
        [0, 0, 1],
        [1, 1, 1]
    ],
    [
        [1, 1, 1],
        [1, 0, 0],
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ],
    [
        [1, 1, 1],
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1]
    ],
    [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ],
    [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
        [0, 0, 1],
        [1, 1, 1]
    ],
    [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
]


class ClockApp(BaseApp):
    name = 'Clock'

    def update(self, dt):
        self.matrix.clear()
        cur_time = datetime.now()
        hour_list = [
            cur_time.hour // 10,
            cur_time.hour % 10
        ]
        min_list = [
            cur_time.minute // 10,
            cur_time.minute % 10
        ]

        x_start = 0#math.floor(self.matrix.WIDTH / 2 - len(time_list) * 4 / 2)
        y_start = self.matrix.HEIGHT-11#math.floor(self.matrix.HEIGHT / 2 - 10 / 2)

        for i in range(len(hour_list)):
            num = num_pix[hour_list[i]]
            for y in range(5):
                for x in range(3):
                    if num[y][x] == 1:
                        x_pos = x_start+i*8+x*2
                        y_pos = y_start+9-y*2
                        if x_pos+1 < self.matrix.WIDTH and y_pos+1 < self.matrix.HEIGHT:
                            self.matrix.set_pixel(x_pos, y_pos, (255, 0, 0))
                            self.matrix.set_pixel(x_pos+1, y_pos, (255, 0, 0))
                            self.matrix.set_pixel(x_pos, y_pos+1, (255, 0, 0))
                            self.matrix.set_pixel(x_pos+1, y_pos+1, (255, 0, 0))

        x_start = self.matrix.WIDTH - 2*7
        y_start = -1
        for i in range(len(min_list)):
            num = num_pix[min_list[i]]
            for y in range(5):
                for x in range(3):
                    if num[y][x] == 1:
                        x_pos = x_start+i*8+x*2
                        y_pos = y_start+9-y*2
                        if x_pos+1 < self.matrix.WIDTH and y_pos+1 < self.matrix.HEIGHT:
                            self.matrix.set_pixel(x_pos, y_pos, (255, 0, 0))
                            self.matrix.set_pixel(x_pos+1, y_pos, (255, 0, 0))
                            self.matrix.set_pixel(x_pos, y_pos+1, (255, 0, 0))
                            self.matrix.set_pixel(x_pos+1, y_pos+1, (125, 0, 0))



