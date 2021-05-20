from Point import Point
import math

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
    
    def rotate_points_abt_center(self, radians):
        
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

    
    def rotate_towards_mouse(self, x ,y):
        radians = self.calc_angle_of_rotation(x, y)
        print(radians)
        self.rotate_points_abt_center(radians)

    def print_points(self):
        for p in self.points:
            print("(" + str(p.x) + "," + str(p.y) + ")")
        print("-------------------")

    def find_rotation_vertex(self):
        #I am calling the rotation vertex the midpoint between the first two points
        self.rotation_point = Point((self.points[0].x + self.points[1].x)/2,(self.points[0].y + self.points[1].y)/2)


    def calc_angle_of_rotation(self, x, y):

        if self.rotation_point == None:
            self.find_rotation_vertex()

        centroid_to_rot = Point(self.rotation_point.x - self.center_point.x, self.rotation_point.y - self.center_point.y)
        centroid_to_mouse = Point( x - self.center_point.x, y - self.center_point.y)

        mag_centroid_to_rot = math.sqrt(centroid_to_rot.x ** 2 + centroid_to_rot.y **2)
        mag_centroid_to_mouse = math.sqrt(centroid_to_mouse.x ** 2 + centroid_to_mouse.y **2)

        dot_over_mags = ((centroid_to_mouse.x * centroid_to_rot.x) + (centroid_to_mouse.y * centroid_to_rot.y)) / (mag_centroid_to_mouse * mag_centroid_to_rot)

        angle = math.acos(dot_over_mags)

        return angle