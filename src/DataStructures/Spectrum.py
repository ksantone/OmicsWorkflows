import Peak
import base64

class Spectrum():
    rt = 0.0
    peak_list = []

    def __init__(self, binary_data):
        self.peak_list = self.construct_peak_list(binary_data)

    def construct_peak_list(self, binary_data):
        pass