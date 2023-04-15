import numpy as np

# define the 3x3 reflection matrix
refl_matrix = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])

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

# example usage: reflect a square about the line y=x
square = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])  # define the square coordinates
reflected_square = reflect_polygon(square)  # reflect the square
print("The reflected square is:\n", reflected_square)  # output the reflected square coordinates
