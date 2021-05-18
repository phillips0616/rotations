from tkinter import *
from Point import Point
from Polygon import Polygon
import time

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
    
    for r in range(len(polygon.points) - 1):
        p1 = translate_point(polygon.points[r])
        p2 = translate_point(polygon.points[r + 1])
        canvas.create_line(p1.x,p1.y, p2.x, p2.y)
    
    last = translate_point(polygon.points[-1])
    first = translate_point(polygon.points[0])
    canvas.create_line(last.x, last.y, first.x, first.y)
    root.update()

def animate_rotation(polygon, degrees):
    for r in range(degrees):
        canvas.delete("all")
        polygon.rotate_points_abt_center(1)
        time.sleep(0.01)
        draw_obj(polygon)


root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas = Canvas(root, width=1000, height=1000)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))

origin_x = 500
origin_y = 500

poly = Polygon([Point(0,0), Point(200,0), Point(100,100)])

draw_obj(poly)

root.update_idletasks()
root.update()

animate_rotation(poly, 360)

root.mainloop()


