Riley Lundquist
Convex Hull Project

Files:
ConvexHull.py contains the main convex hull program. It implements the divide and conquer algorithm to solve the convex hull problem. Documentation of methods is included in the file.

Hull.py is an implementation of a circular list (Python's equivalent of an array). This is used for indexing the data in a circular manner, allowing accesses beyond the bounds of the list. Documentation of the class and its methods is included in the file.

Point.py is a class which stores coordinate pairs. It contains methods which tell (counter)clockwise relationships between points and line segments (represented as pairs of points). Documentation of the class and its methods is included in the file.

Running the Program:
Copy test data files into the Convex Hull folder where this file was found. Open the Python Launcher application. From the Python Launcher File menu, select Open, and open ConvexHull.py from the Convex Hull folder. When prompted, enter the name of the file containing the test data (the file should be in the Convex Hull folder). The program will print the points on the convex hull of the set of points in counterclockwise order.