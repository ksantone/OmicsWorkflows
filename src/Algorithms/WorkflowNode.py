class WorkflowNode():
    in_edges = dict()
    out_edges = dict()
    in_data = dict()
    # If not using HPC can_start will immediately be set to True, otherwise send an email to the user
    # and when they have provided necessary information allow it to begin
    can_start = False

    def __init__(self, name, in_edges, out_edges, algorithm, can_start):
        self.name = name
        for in_edge in in_edges:
            self.in_edges[in_edge.name] = in_edge
        for out_edge in out_edges:
            self.out_edges[out_edge.name] = out_edge
        self.algorithm = algorithm
        self.can_start = can_start

    def dependent_edge_completed(self, in_edge, data):
        self.in_edges.pop(in_edge.name)
        self.in_data[in_edge.name] = data
        if not self.in_edges and self.can_start:
            self.execute_algorithm(self.algorithm)

    def execute_algorithm(self, algorithm):
        # Find a way of passing the algorithm to a C++ API where it can be executed more efficiently
        # than with Python
        algorithm.call_executable(algorithm.name)