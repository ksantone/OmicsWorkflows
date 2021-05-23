import xml.etree.ElementTree as ET
from pathlib import Path

from src.DataPreprocessing.OpenProcessor import OpenProcessor
from src.DataStructures import Spectrum

class MzMLProcessor(OpenProcessor):
    instrument = ""
    spectrum_list = []
    chromatogram_list = []
    mzml_tree = None
    mzml_root = None

    def __init__(self, file_name, peak_map, data_logger):
        home_dir = str(Path.home())
        abs_file_name = home_dir + file_name
        self.mzml_tree = ET.parse(abs_file_name)
        self.mzml_root = self.mzml_tree.getroot()
        super.__init__(self, file_name, peak_map, data_logger)

    def find_instrument(self, abs_file_name):
        instrument_model = self.mzml_root.findall("./instrumentConfigurationList/instrumentConfiguration/cvParam")

    def construct_spectrum_list(self, abs_file_name, data_logger):
        spectra_list = []
        spectra_to_binary_data = dict()
        spectra_to_cv_params = dict()

        for spectrum in self.mzml_root.findall("./run/spectrumList/spectrum"):
            spectra_list.append(spectrum)
            cv_params = []
            binary_data = []
            for cvParam in spectrum.findall("./cvParam"):
                cv_params.append(cvParam)
            for binaryDataList in spectrum.findall("./binaryDataArrayList"):
                binary_data.append(binaryDataList)
            spectra_to_binary_data[spectrum] = binary_data
            spectra_to_cv_params[spectrum] = cv_params

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