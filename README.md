Convex Hull
===========

Riley Lundquist

May, 2013

Files:

ConvexHull.py contains the main convex hull program. It implements the divide and conquer algorithm to solve the convex hull problem. Documentation of methods is included in the file.

Hull.py is an implementation of a circular list (Python's equivalent of an array). This is used for indexing the data in a circular manner, allowing accesses beyond the bounds of the list. Documentation of the class and its methods is included in the file.

Point.py is a class which stores coordinate pairs. It contains methods which tell (counter)clockwise relationships between points and line segments (represented as pairs of points). Documentation of the class and its methods is included in the file.

Running the Program:
--------------------
Copy test data files into the folder where this file and the other program files were found. To run:

```
$ python ConvexHull.py
```

You will then be prompted for the name of a data file. Enter the name of the file, and the program will print the points on the convex hull in counterclockwise order:

```
Enter name of file containing data set (e.g. test.txt or points.dat):
10000n.dat
(-3.97683835029602, 0.0402181185781956)
(-3.09143090248108, -1.98761200904846)
(-1.11660432815552, -4.23753499984741)
(0.602447986602783, -3.84486389160156)
(2.15539765357971, -3.03128695487976)
(3.73647785186768, -1.53223466873169)
(4.15127563476562, -0.851924538612366)
(3.97476863861084, 0.851975083351135)
(3.1648588180542, 2.44896554946899)
(1.80845034122467, 4.08591270446777)
(-1.82051539421082, 3.65553545951843)
(-3.19176483154297, 2.30337738990784)
```
