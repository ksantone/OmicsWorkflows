import Peptide, Spectrum

class PeptideSpectrumMatch():
    peptide = None
    spectrum = None
    p_value = 0.0
    e_value = 0.0
    is_decoy = False

    def __init__(self, peptide, spectrum, is_decoy):
        self.peptide = peptide
        self.spectrum = spectrum
        p_value = self.compute_p_value(peptide, spectrum)
        e_value = self.compute_e_value(p_value)

    def compute_p_value(self, peptide, spectrum):
        pass

    def compute_e_value(self, p_value):
        pass