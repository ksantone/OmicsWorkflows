from src.Algorithms import Workflow, WorkflowEdge, WorkflowNode, DeNovoAlgorithm, FeatureDetectionAlgorithm, SpectralAlignmentAlgorithm

class DDAPipeline(WorkflowNode):
    generate_spectral_library = False

    def __init__(self, file_list, generate_spectral_library):
        pass