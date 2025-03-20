import trimesh
import numpy as np

# Load the mesh (even if it only has vertices)
mesh = trimesh.load("mesh_selected_inner_points.obj")

# Get the vertices as a point cloud
points = mesh.vertices

# Save as a simple point cloud format
np.savetxt("output.xyz", points)