from Point import Point
import math

class Polygon:
    def __init__(self, points=[]):
        self.points = points
        self.center_point = self.calc_centroid()
    
    def add_point(self,x,y):
        p = Point(x,y)
        self.points.append(p)

    def rotate_points_abt_axis(self, degree):
        radians = math.radians(degree)

        print(radians)
        
        for p in self.points:
            x = p.x
            y = p.y

            p.x = x*math.cos(radians) - y*math.sin(radians)
            p.y = x*math.sin(radians) + y*math.cos(radians)
    
    def rotate_points_abt_center(self, degree):
        radians = math.radians(degree)
        
        for p in self.points:
            x = p.x
            y = p.y

            center_diff_x = x - self.center_point.x
            center_diff_y = y - self.center_point.y

            p.x = center_diff_x*math.cos(radians) - center_diff_y*math.sin(radians) + self.center_point.x
            p.y = center_diff_x*math.sin(radians) + center_diff_y*math.cos(radians) + self.center_point.y
    

    def calc_centroid(self):
        sum_x = 0
        sum_y = 0
        for p in self.points:
            sum_x += p.x
            sum_y += p.y
        
        return Point(sum_x / len(self.points), sum_y / len(self.points))