import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from dataclasses import dataclass
from typing import List, Tuple

import matplotlib.pyplot as plt

@dataclass
class Landmark:
    name: str
    position: np.ndarray
    description: str = ""

class CraniofacialModel:
    def __init__(self):
        self.landmarks: List[Landmark] = []
        self.mesh_vertices = np.array([])
        self.mesh_faces = np.array([])
    
    def add_landmark(self, name: str, position: Tuple[float, float, float], 
                     description: str = ""):
        """Add anatomical landmark"""
        landmark = Landmark(name, np.array(position), description)
        self.landmarks.append(landmark)
    
    def load_mesh(self, vertices: np.ndarray, faces: np.ndarray):
        """Load 3D mesh data"""
        self.mesh_vertices = vertices
        self.mesh_faces = faces
    
    def visualize(self, show_landmarks: bool = True, show_mesh: bool = True):
        """3D visualization with annotations"""
        fig = plt.figure(figsize=(12, 9))
        ax = fig.add_subplot(111, projection='3d')
        
        if show_mesh and len(self.mesh_vertices) > 0:
            ax.plot_trisurf(self.mesh_vertices[:, 0], 
                           self.mesh_vertices[:, 1],
                           self.mesh_vertices[:, 2],
                           alpha=0.3, edgecolor='gray')
        
        if show_landmarks:
            for landmark in self.landmarks:
                ax.scatter(*landmark.position, s=100, c='red', marker='o')
                ax.text(landmark.position[0], landmark.position[1], 
                       landmark.position[2], landmark.name, fontsize=9)
        
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('Craniofacial Model')
        plt.show()
    
    def get_distance(self, landmark1: str, landmark2: str) -> float:
        """Calculate distance between landmarks"""
        l1 = next((l for l in self.landmarks if l.name == landmark1), None)
        l2 = next((l for l in self.landmarks if l.name == landmark2), None)
        
        if l1 and l2:
            return np.linalg.norm(l1.position - l2.position)
        return 0.0

# Example usage
model = CraniofacialModel()
model.add_landmark("Nasion", (0, 10, 0), "Bridge of nose")
model.add_landmark("Pogonion", (0, 0, -5), "Chin prominence")
model.add_landmark("Menton", (0, -2, -6), "Lowest point of chin")

print(f"Distance Nasion-Pogonion: {model.get_distance('Nasion', 'Pogonion'):.2f} mm")

model.visualize()
