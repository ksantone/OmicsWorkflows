import Ion

class PrecursorIon(Ion):
    mono_mz = 0.0
    rt = 0.0
    intensity = 0.0
    parent_spec = None
    tandem_spec = None

    def __init__(self, mz, rt, intensity, parent_spec, tandem_spec):
        super.__init__(self, mz, rt, intensity)
        self.parent_spec = parent_spec
        self.tandem_spec = tandem_spec