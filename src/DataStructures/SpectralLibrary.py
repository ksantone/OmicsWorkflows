import Peptide, Spectrum

class SpectralLibrary():
    spectral_library = []
    real_peptides = []
    decoy_peptides = []

    def __init__(self, spectral_library):
        self.spectral_library = spectral_library
        self.real_peptides = self.find_real_peptides(spectral_library)
        self.decoy_peptides = self.find_decoy_peptides(spectral_library)

    def find_real_peptides(self, spectral_library):
        pass

    def find_decoy_peptides(self, spectral_library):
        pass