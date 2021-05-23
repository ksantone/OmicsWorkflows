class Ion():
    mono_mz = 0.0
    rt = 0.0
    intensity = 0.0

    def __init__(self, mz, rt, intensity):
        self.mz = mz
        self.rt = rt
        self.intensity = intensity