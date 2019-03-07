def deform_grid(self):
		#This function deforms the grid as per the algorithm
		for node in self.pixel_graph.nodes_iter():
			self.deform_cell(node) # Iterate through all the nodes in the graph and deform each of them

		# Collapse all valence-2 nodes to get a more smoother image
		removals = []
		for node in self.grid_graph.nodes_iter():
			if node in ((0, 0), (0, self.size[1]),
						(self.size[0], 0), self.size):
				# Skip corner nodes of teh image as they shouldn't be collapsed, obviously!
				continue
			neighbors = self.grid_graph.neighbors(node)
			if len(neighbors) == 2: #Connect the neighbors of the valence-2 node by an edge
				self.grid_graph.add_edge(*neighbors)
			if len(neighbors) <= 2:
				removals.append(node)
