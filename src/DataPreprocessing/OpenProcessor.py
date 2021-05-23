from pathlib import Path
from src.DataStructures import Spectrum

class OpenProcessor():
    instrument = ""
    spectrum_list = []
    chromatogram_list = []

    def __init__(self, file_name, peak_map, data_logger):
        home_dir = str(Path.home())
        abs_file_name = home_dir + file_name
        self.instrument = self.find_instrument(abs_file_name)
        self.spectrum_list = self.construct_spectrum_list(abs_file_name, data_logger)
        self.set_spectra_in_peak_map(self.spectrum_list, peak_map)
        self.chromatogram_list = self.construct_chromatogram_list(abs_file_name, data_logger)
        self.set_chromatogram_in_peak_map(self.chromatogram_list, peak_map)

    def find_instrument(self, abs_file_name):
        # This may be independent of file extension but I haven't looked into it yet
        return ""

    def construct_spectrum_list(self, abs_file_name, data_logger):
        # This will vary depending on what the extension of the file is thus is only instantiated in subclasses
        # The data_logger variable will have start_progress called on it right at the start then it will increment
        # until all spectra have been determined
        return []

    def set_spectra_in_peak_map(self, spectrum_list, peak_map):
        for spectrum in spectrum_list:
            peak_map.add_spectrum(spectrum)

    def construct_chromatogram_list(self, abs_file_name, data_logger):
        # This will vary depending on what the extension of the file is thus is only instantiated in subclasses
        # The data_logger variable will have start_progress called on it right at the start then it will increment
        # until all spectra have been determined
        return []

    def set_chromatograms_in_peak_map(self, chromatograms_list, peak_map):
        for chromatogram in chromatograms_list:
            peak_map.add_chromatogram(chromatogram)