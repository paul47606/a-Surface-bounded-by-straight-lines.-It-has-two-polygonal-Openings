import matplotlib.pyplot as plt

# given points
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

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the points as a scatter plot
# here 0 = x, 1 = y, z = 2
ax.scatter(Point1[0], Point1[1], Point1[2], c='r')
ax.scatter(Point2[0], Point2[1], Point2[2], c='r')
ax.scatter(Point3[0], Point3[1], Point3[2], c='r')
ax.scatter(Point4[0], Point4[1], Point4[2], c='r')
ax.scatter(Point5[0], Point5[1], Point5[2], c='r')
ax.scatter(Point6[0], Point6[1], Point6[2], c='r')
ax.scatter(Point7[0], Point7[1], Point7[2], c='k')
ax.scatter(Point8[0], Point8[1], Point8[2], c='k')
ax.scatter(Point9[0], Point9[1], Point9[2], c='k')
ax.scatter(Point10[0], Point10[1], Point10[2], c='k')
ax.scatter(Point11[0], Point11[1], Point11[2], c='k')
ax.scatter(Point12[0], Point12[1], Point12[2], c='y')
ax.scatter(Point13[0], Point13[1], Point13[2], c='y')
ax.scatter(Point14[0], Point14[1], Point14[2], c='y')
ax.scatter(Point15[0], Point15[1], Point15[2], c='y')

# Set the axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()