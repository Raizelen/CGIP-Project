import numpy as np
import turtle

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

# create a Turtle window
wn = turtle.Screen()
wn.bgcolor('black')
wn.setworldcoordinates(-9, -9, 9, 9)  # set the coordinates of the turtle window

# create a Turtle to draw the x-axis
x_axis = turtle.Turtle()
x_axis.color("white")
x_axis.penup()
x_axis.goto(-10, 0)
x_axis.pendown()
x_axis.goto(10, 0)
x_axis.write("X", font=("Arial", 10, "bold"))  # label the x-axis

# create a Turtle to draw the y-axis
y_axis = turtle.Turtle()
y_axis.color("white")
y_axis.penup()
y_axis.goto(0, -10)
y_axis.pendown()
y_axis.goto(0, 10)
y_axis.write("Y", font=("Arial", 10, "bold"))  # label the y-axis

# create a Turtle to draw the original polygon
t1 = turtle.Turtle()
t1.color("red")
t1.penup()
t1.goto(polygon[0][0], polygon[0][1])
t1.pendown()
for i in range(1, len(polygon)):
    t1.goto(polygon[i][0], polygon[i][1])
t1.goto(polygon[0][0], polygon[0][1])
t1.write("Original", font=("Arial", 10, "normal"))  # label the original polygon


# create a Turtle to draw the reflected polygon
t2 = turtle.Turtle()
t2.color("blue")
t2.penup()
t2.goto(reflected_polygon[0][0], reflected_polygon[0][1])
t2.pendown()
for i in range(1, len(reflected_polygon)):
    t2.goto(reflected_polygon[i][0], reflected_polygon[i][1])
t2.goto(reflected_polygon[0][0], reflected_polygon[0][1])
t2.write("Reflected", font=("Arial", 10, "normal"))  # label the reflected polygon


# keep the Turtle window open until the user closes it
wn.mainloop()
