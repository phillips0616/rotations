from Point import Point
import math
import time

class Polygon:
    def __init__(self, points=[]):
        self.points = points
        self.center_point = None
        self.rotation_point = None
    
    def add_point(self,p):
        insert_index = 0
        foundclock = False
        for p2 in self.points:
            clock = self.clockwise(p, p2) 
            if clock:
                foundclock = True
            if not clock and foundclock:
                break
            insert_index += 1
        
        self.points.insert(insert_index, p)

        self.calc_centroid()
        
    def clockwise(self, p1, p2):

        determinate = p1.x*p2.y - p1.y*p2.x

        if determinate > 0:
            return True
        elif determinate < 0:
            return False
        else:
            #this should be a calculation
            return True

    def rotate_points_abt_axis(self, degree):
        radians = math.radians(degree)

        print(radians)
        
        for p in self.points:
            x = p.x
            y = p.y

            p.x = x*math.cos(radians) - y*math.sin(radians)
            p.y = x*math.sin(radians) + y*math.cos(radians)
    
    def rotate_points_abt_center(self, radians, direction):
        angle = radians
        #interpolate rotation

        # for r in range(10):
        #     angle = (radians / (10 - r + 1))
        for p in self.points:
            x = p.x
            y = p.y

            p.x , p.y = self.get_rotated_point_values(p, angle, direction)
    
    def get_rotated_point_values(self, p, radians, direction):
        x = p.x
        y = p.y

        center_diff_x = x - self.center_point.x
        center_diff_y = y - self.center_point.y

        if direction == "counter":
            x = center_diff_x*math.cos(radians) - center_diff_y*math.sin(radians) + self.center_point.x
            y = center_diff_x*math.sin(radians) + center_diff_y*math.cos(radians) + self.center_point.y
        else:
            x = center_diff_x*math.cos(radians) + center_diff_y*math.sin(radians) + self.center_point.x
            y = -1*center_diff_x*math.sin(radians) + center_diff_y*math.cos(radians) + self.center_point.y 
        return x, y

    def calc_centroid(self):
        sum_x = 0
        sum_y = 0
        for p in self.points:
            sum_x += p.x
            sum_y += p.y
        
        self.center_point = Point(sum_x / len(self.points), sum_y / len(self.points))

    
    def rotate_towards_mouse(self, x ,y, prev_x, prev_y):
        radians = self.calc_angle_of_rotation(x, y, prev_x, prev_y)
        print(radians)
        if y - prev_y > 0:
            self.rotate_points_abt_center(radians, "counter")
        else:
            self.rotate_points_abt_center(radians, "clockwise")

    def print_points(self):
        for p in self.points:
            print("(" + str(p.x) + "," + str(p.y) + ")")
        print("-------------------")


    def calc_angle_of_rotation(self, x, y, prev_x, prev_y):

       

        centroid_to_prev = Point(prev_x - self.center_point.x, prev_y - self.center_point.y)
        centroid_to_cur = Point( x - self.center_point.x, y - self.center_point.y)

        mag_centroid_to_rot = math.sqrt(centroid_to_prev.x ** 2 + centroid_to_prev.y **2)
        mag_centroid_to_mouse = math.sqrt(centroid_to_cur.x ** 2 + centroid_to_cur.y **2)

        dot_over_mags = ((centroid_to_prev.x * centroid_to_cur.x) + (centroid_to_prev.y * centroid_to_cur.y)) / (mag_centroid_to_mouse * mag_centroid_to_rot)

        #the weight allows it to rotate faster (less mouse dragging)
        weight = 20
        angle = math.acos(dot_over_mags)*weight

        # adj = abs(x - self.center_point.x)
        # hyp = math.sqrt(adj ** 2 + (self.center_point.y - y) ** 2)

        # angle = math.acos(adj / hyp)

        return angle