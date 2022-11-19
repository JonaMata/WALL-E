import time

from .BaseApp import BaseApp

import math
import pyaudio
import numpy as np
from time import perf_counter

pa = pyaudio.PyAudio()

sample_rate = 44100
buff_size = 1024

bars = 14
lerp_speed = 0.5
scaling_factor = 1.1

freq_bars = [
    50,
    100,
    150,
    200,
    300,
    400,
    500,
    750,
    1250,
    2000,
    3000,
    4000,
    6000,
    8000,
]

speed = 3


def wheel(pos):
    pos = pos % 255
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return r, g, b


class MusicApp(BaseApp):
    def __init__(self, matrix):
        super().__init__(matrix)

        self.pa = pyaudio.PyAudio()
        self.input_data = []
        self.prev_state = [0 for _ in range(bars)]
        self.offset = 0
        self.mes_vals = [1 for _ in range(bars)]
        self.prev_max = []
        self.prev_beat = 0
        self.low_freq_avg_list = []

        self.input_device = pa.get_device_info_by_host_api_device_index(0, pa.get_host_api_info_by_index(0)[
            'defaultInputDevice'])

        self.stream = pa.open(format=pyaudio.paInt16,
                              channels=1,
                              rate=sample_rate,
                              output=False,
                              input=True,
                              stream_callback=self.callback,
                              input_device_index=self.input_device['index'])

        self.stream.start_stream()

    def callback(self, in_data, frame_count, time_info, flag):
        audio_data = np.frombuffer(in_data, dtype=np.int16)
        self.input_data = np.append(self.input_data, audio_data)
        self.input_data = self.input_data[-buff_size:]
        return None, pyaudio.paContinue

    def update(self, dt):
        if self.stream.is_active():
            if len(self.input_data) == buff_size:
                # Calc FFT data
                data = self.input_data.copy()
                fft_data = np.abs(np.fft.rfft(data))
                fft_freq = np.fft.rfftfreq(data.size, d=1 / sample_rate)

                # Clear matrix
                self.matrix.fill((0, 0, 0))

                #
                for i in range(bars):
                    max_freq = freq_bars[i]
                    for j in range(len(fft_freq)):
                        # Calc value when freq range for bar is found
                        if fft_freq[j] > max_freq:
                            if j > 0:
                                val = max([max(fft_data[x:x+4]) for x in range(0, j, 4)])
                                fft_freq = fft_freq[j:]
                                fft_data = fft_data[j:]
                                val = val * np.power(scaling_factor, i + 1) - .05
                                self.mes_vals[i] = val
                                val = val / max(self.prev_max)
                                val = min(math.floor(val * 22), 22)

                                # Linear Interpolation
                                prev = self.prev_state[i]
                                if val > prev:
                                    val = prev + math.floor((val - prev) * lerp_speed)
                                elif val < prev:
                                    val = prev - math.floor((prev - val) * lerp_speed)
                                self.prev_state[i] = val

                                # Load into pixels
                                for y in range(val):
                                    width = int(self.matrix.WIDTH / bars)
                                    for k in range(width):
                                        x = i * width + k
                                        self.matrix.set_pixel(x, y, wheel(x + y + self.offset))
                            break

        self.prev_max.append(max(self.mes_vals))
        self.prev_max = self.prev_max[-50:]

        # Beat detection
        low_freq_avg = np.average(self.mes_vals[0:8])
        self.low_freq_avg_list.append(low_freq_avg)
        avg = np.average(self.low_freq_avg_list)
        bass_avg = np.average(self.mes_vals[0:4])
        if avg > 10 and (bass_avg > avg * 1.5 or (low_freq_avg < avg * 1.2 and bass_avg > avg)):
            this_beat = perf_counter()
            if this_beat - self.prev_beat > 60/180:
                self.offset += 125
                self.prev_beat = this_beat
        self.low_freq_avg_list = self.low_freq_avg_list[-50:]
        self.offset = (self.offset + speed) % 255

    def exit(self):
        self.stream.close()
