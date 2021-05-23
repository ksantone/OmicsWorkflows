class Feature():
    mono_mz = 0.0
    rt = 0.0
    isotopes = 0
    def __init__(self, mono_mz, rt, isotopes):
        self.mono_mz = mono_mz
        self.rt = rt
        self.isotopes = isotopes