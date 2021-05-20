from tkinter import *
from Point import Point
from Polygon import Polygon
from Sketchpad import Sketchpad
import time
import random

lines = []
def translate_point(p):
    return Point(p.x + origin_x, origin_y - p.y)

def draw_lines(polygon,color=None):
    for line in polygon.lines:
        p1 = translate_point(line.start_point)
        p2 = translate_point(line.end_point)
        if color != None:
            fill = color
        else:
            fill = line.color
        canvas.create_line((p1.x, p1.y, p2.x, p2.y), width=3, fill=fill)

def draw_obj(polygon):
    clear_lines()
    colors = ['red', 'blue', 'green', 'orange', 'pink', 'yellow', "brown", "sea green", "orange red", "SlateBlue2", "PaleTurquoise2", "khaki1", "coral1"]
    for r in range(len(polygon.points) - 1):
        p1 = translate_point(polygon.points[r])
        p2 = translate_point(polygon.points[r + 1])
        color = colors[random.randint(0,len(colors) - 1)]
        line = canvas.create_line(p1.x,p1.y, p2.x, p2.y, fill=color)
        lines.append(line)
    
    color = colors[random.randint(0,len(colors) - 1)]
    last = translate_point(polygon.points[-1])
    first = translate_point(polygon.points[0])
    line = canvas.create_line(last.x, last.y, first.x, first.y, fill=color)
    lines.append(line)
    root.update()

def animate_rotation(event):
    polygon = poly
    poly.calc_centroid()
    degrees = 360
    for r in range(degrees):
        #canvas.delete("all")
        polygon.rotate_points_abt_center(1)
        time.sleep(0.01)
        draw_obj(polygon)

def make_point(event):
    p = Point(event.x - origin_x, origin_y - event.y)
    poly.add_point(p)
    canvas.create_oval(event.x -5, event.y - 5, event.x + 5, event.y + 5, fill="black")
    poly.print_points()
    if len(poly.points) >= 3:
        print("redrawing....")
        draw_obj(poly)

def clear_lines():
    #I think there is an issue with deleting from this list while
    #iterating over it...
    for line in lines:
        canvas.delete(line)
    lines.clear()

root = Tk()
root.geometry("1000x1000")
root.update_idletasks()

sketchpad = Sketchpad(root, 500, 500)
sketchpad.pack(expand=True, fill='both')

canvas = Canvas(root, width=1000, height=1000)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))

# animate_rotation(poly, 360)

root.mainloop()


