from Point import Point
import math

class Polygon:
    def __init__(self, points=[]):
        self.points = points
        self.center_point = None#self.calc_centroid()
    
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
        
        self.center_point = Point(sum_x / len(self.points), sum_y / len(self.points))

    def print_points(self):
        for p in self.points:
            print("(" + str(p.x) + "," + str(p.y) + ")")
        print("-------------------")