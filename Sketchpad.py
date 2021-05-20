from tkinter import *
from Polygon import Polygon
from Point import Point
import time

class Sketchpad(Canvas):
    def __init__(self, parent, origin_x, origin_y):
        super().__init__(parent, bg="white")
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.polygon = Polygon()
        self.canvas_objs = {"vertices": [], "lines": []}
        self.bind("<Button-1>", self.make_point)
        self.bind("<Button-3>", self.complete_polygon)
        self.bind("<B1-Motion>", self.animate_rotation)
        self.rotation = False
        self.prev_x_mouse_pos = None
        self.prev_y_mouse_pos = None

    
    def translate_point(self, p):
        return Point(p.x + self.origin_x, self.origin_y - p.y)
    
    def complete_polygon(self, event):

        self.polygon.calc_centroid()

        self.unbind("<Button-1>")
        
        self.rotation = True


    def animate_rotation(self, event):
        if self.rotation:
            point = self.translate_point(Point(event.x, event.y))

            if self.prev_x_mouse_pos == None or self.prev_y_mouse_pos == None:
                self.prev_x_mouse_pos = event.x
                self.prev_y_mouse_pos = event.y
            
            prev_point = self.translate_point(Point(self.prev_x_mouse_pos, self.prev_y_mouse_pos))

            self.polygon.rotate_towards_mouse(point.x,point.y, prev_point.x, prev_point.y)

            self.prev_x_mouse_pos = event.x
            self.prev_y_mouse_pos = event.y

            self.draw_polygon()

    def make_point(self, event):
        p = Point(event.x - self.origin_x, self.origin_y - event.y)
        self.polygon.add_point(p)
        vertex = self.create_oval(event.x -3, event.y - 3, event.x + 3, event.y + 3, fill="black")
        self.canvas_objs["vertices"].append(vertex)
        if len(self.polygon.points) >= 3:
            print("redrawing....")
            self.draw_polygon()
    
    def draw_polygon(self):
        self.clear_sketchpad()

        for r in range(len(self.polygon.points) - 1):
            
            p1 = self.translate_point(self.polygon.points[r])
            p2 = self.translate_point(self.polygon.points[r + 1])
                
            line = self.create_line(p1.x,p1.y, p2.x, p2.y)
            self.canvas_objs["lines"].append(line)

            vertex1 = self.create_oval(p1.x -3, p1.y - 3, p1.x + 3, p1.y + 3, fill="black")
            self.canvas_objs["vertices"].append(vertex1)

            vertex2 = self.create_oval(p1.x -3, p1.y - 3, p1.x + 3, p1.y + 3, fill="black")
            self.canvas_objs["vertices"].append(vertex2)
        
        last = self.translate_point(self.polygon.points[-1])
        first = self.translate_point(self.polygon.points[0])
        line = self.create_line(last.x, last.y, first.x, first.y)

        vertex1 = self.create_oval(last.x -3, last.y - 3, last.x + 3, last.y + 3, fill="black")
        self.canvas_objs["vertices"].append(vertex1)

        vertex2 = self.create_oval(first.x -3, first.y - 3, first.x + 3, first.y + 3, fill="black")
        self.canvas_objs["vertices"].append(vertex2)

        self.canvas_objs["lines"].append(line)
    
    def clear_sketchpad(self):
        self.delete("all")

        #self.bind("<Button-1>", self.make_point)

        self.canvas_objs = {"vertices": [], "lines": []}

