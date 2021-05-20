from tkinter import *
from Polygon import Polygon
from Point import Point
from ColorPicker import ColorPicker
import time

class Sketchpad:
    def __init__(self, parent, origin_x, origin_y):
        super().init(parent, bg="white")
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.polygons = {}
        self.color_picker = ColorPicker()
        self.bind("<Button-1>", self.make_point)
        self.bind("<Button-3>", self.animate_rotation)

    
    def translate_point(self, p):
        return Point(p.x + self.origin_x, self.origin_y - p.y)


    def animate_rotation(self, polygon, event):
        polygon.calc_centroid()
        degrees = 360
        for r in range(degrees):
            #canvas.delete("all")
            polygon.rotate_points_abt_center(1)
            time.sleep(0.01)
            draw_obj(polygon)

    def make_point(self, polygon, event):
        p = Point(event.x - origin_x, origin_y - event.y)
        poly.add_point(p)
        canvas.create_oval(event.x -5, event.y - 5, event.x + 5, event.y + 5, fill="black")
        poly.print_points()
        if len(poly.points) >= 3:
            print("redrawing....")
            draw_obj(poly)
    
    def draw_polygon(self, polygon, should_remove_lines=True, should_random_colors=False):
        if should_remove_lines:
            self.remove_lines(polygon)

        for r in range(len(polygon.points) - 1):
            
            p1 = self.translate_point(polygon.points[r])
            p2 = self.translate_point(polygon.points[r + 1])

            color = "black"
            if should_random_colors:
                color = self.color_picker.get_random_color()
                
            line = self.create_line(p1.x,p1.y, p2.x, p2.y, fill=color)
            self.polygons[polygon]
            
        
        color = colors[random.randint(0,len(colors) - 1)]
        last = translate_point(polygon.points[-1])
        first = translate_point(polygon.points[0])
        line = canvas.create_line(last.x, last.y, first.x, first.y, fill=color)
        lines.append(line)
        root.update()

    
    def remove_lines(self, polygon):
        lines = self.polygons[polygon]
        for line in lines:
            self.delete(line)
        lines.clear()