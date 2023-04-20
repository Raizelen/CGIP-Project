import numpy as np
import matplotlib.pyplot as plt

# define the 3x3 reflection matrix
refl_matrix = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])

# define a function to prompt the user for polygon coordinates
def get_polygon():
    num_vertices = int(input("Enter the number of vertices in the polygon: "))
    vertices = []
    for i in range(num_vertices):
        x = float(input(f"Enter x-coordinate of vertex {i+1}: "))
        y = float(input(f"Enter y-coordinate of vertex {i+1}: "))
        vertices.append([x, y])
    return np.array(vertices)

# define a function to perform the reflection on a polygon
def reflect_polygon(polygon):
    # convert the polygon coordinates to a 3xN array (adding a row of 1s)
    polygon_3d = np.vstack((polygon.T, np.ones((1, polygon.shape[0]))))
    
    # apply the reflection transformation
    reflected_polygon_3d = np.matmul(refl_matrix, polygon_3d)
    
    # convert the reflected polygon coordinates back to a 2xN array
    reflected_polygon = reflected_polygon_3d[:2, :].T
    
    # return the reflected polygon coordinates
    return reflected_polygon

# prompt the user for polygon coordinates
polygon = get_polygon()

# reflect the polygon
reflected_polygon = reflect_polygon(polygon)

# plot the original and reflected polygons
plt.figure(figsize=(6, 6))
plt.plot(polygon[:, 0], polygon[:, 1], 'r-', label='Original')
plt.plot(reflected_polygon[:, 0], reflected_polygon[:, 1], 'b-', label='Reflected')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis('equal')
plt.legend()
plt.show()

