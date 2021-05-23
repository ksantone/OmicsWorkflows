from src.DataStructures import Ion, FragmentIon, Spectrum
import os, subprocess

class DeNovoAlgorithm():
    executable_name = "Executables/DeNovoAlgorithm.exe"
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

    def __init__(self, path_to_executable):
        path_to_executable = os.path.join(self.ROOT_DIR, self.executable_name)
        self.call_executable(path_to_executable)

    def call_executable(self, executable_name):
        self.denovo_algorithm_output = subprocess.run(executable_name)