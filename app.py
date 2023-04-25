import numpy as np
import turtle
from flask import Flask, render_template, request

app = Flask(__name__)

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

# define a function to draw the polygon using Turtle graphics
def draw_polygon(turtle, polygon, color):
    turtle.penup()
    turtle.goto(polygon[0][0], polygon[0][1])
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(1, len(polygon)):
        turtle.goto(polygon[i][0], polygon[i][1])
    turtle.goto(polygon[0][0], polygon[0][1])
    turtle.end_fill()

# define a function to draw the x-axis using Turtle graphics
def draw_x_axis(turtle):
    turtle.penup()
    turtle.goto(-10, 0)
    turtle.pendown()
    turtle.goto(10, 0)

# define a function to draw the y-axis using Turtle graphics
def draw_y_axis(turtle):
    turtle.penup()
    turtle.goto(0, -10)
    turtle.pendown()
    turtle.goto(0, 10)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # get the number of vertices from the form
        num_vertices = int(request.form.get('num_vertices'))

        # get the polygon coordinates from the form
        vertices = []
        for i in range(num_vertices):
            x = float(request.form.get(f'vertex_{i+1}_x'))
            y = float(request.form.get(f'vertex_{i+1}_y'))

            vertices.append([x, y])
        polygon = np.array(vertices)
        
        
        # reflect the polygon
        reflected_polygon = reflect_polygon(polygon)

        # create a Turtle window
        wn = turtle.Screen()
        wn.setworldcoordinates(-10, -10, 10, 10)

        # draw the x-axis and y-axis
        draw_x_axis(turtle.Turtle())
        draw_y_axis(turtle.Turtle())

        # draw the original polygon and the reflected polygon
        draw_polygon(turtle.Turtle(), polygon, 'blue')
        draw_polygon(turtle.Turtle(), reflected_polygon, 'red')

        # keep the Turtle window open until the user closes it
        wn.mainloop()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
