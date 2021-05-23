class WorkflowEdge():
    in_node = None
    out_nodes = dict()
    out_data = dict()
    name = ""

    def __init__(self, name, in_node, out_nodes):
        self.name = name
        self.in_node = in_node
        for out_node in out_nodes:
            self.out_nodes[out_node.name] = out_node
            self.data_for_algorithm(out_node)

    def data_for_algorithm(self, out_node):
        # Determine what data is needed for the node this edge is pointing at pass it in and remove
        # this edge from the list of edges the node is waiting on
        output_data = None
        # If requires additional resources email user to provide it before executing next algorithm
        out_node.dependent_edge_completed(self, output_data)