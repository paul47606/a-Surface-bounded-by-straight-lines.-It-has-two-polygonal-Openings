# based on the given table x axis range from = '-1.0 to 9' and z axis range from = '-2.0 to 6.0'
# and y is 0 - this are considred from pints 1 to 6 only



x_minimum = -1.0
x_maxinum = 9

z_minimum = -2.0
z_maximun = 6.0



# Given points
Point1 = (0.0, 0.0, 0.0)
Point2 = (4.0, 0.0, -2.0)
Point3 = (9.0, 0.0, 0.0)
Point4 = (9.0, 0.0, 5.0)
Point5 = (5.0, 0.0, 6.0)
Point6 = (-1.0, 0.0, 4.5)
Point7 = (0.1, 0.0, 2.8)
Point8 = (0.4, 0.0, 1.4)
Point9 = (2.6, 0.0, -0.5)
Point10 = (3.1, 0.0, 0.5)
Point11 = (1.6, 0.0, 2.4)
Point12 = (4.0, 0.0, 3.0)
Point13 = (6.0, 0.0, 1.0)
Point14 = (7.0, 0.0, 3.0)
Point15 = (5.0, 0.0, 4.0)

# Check which points are inside the bounding box
inside_points = []
for point in [Point7, Point8, Point9, Point10, Point11, Point12, Point13, Point14, Point15]:
    x, y, z = point
    if x_minimum <= x <= x_maxinum and z_minimum <= z <= z_maximun:
        inside_points.append(point)

# Print the points that are inside the bounding box
if len(inside_points) > 0:
    print("The following points are inside the bounding box:")
    for point in inside_points:
        print(point)
else:
    print("There are no points out side the bounding box.")
