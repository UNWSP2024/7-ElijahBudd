# Elijah Budd
# 3/6/2025
# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input)
# and will return (as output) the distance between those points in space.
# The 3-dimensional coordinates must be stored as tuples.

# Now write a mainline that has the user enter the two tuples.
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2)
import math

def distance(coordinates1, coordinates2):
    x1, y1, z1 = coordinates1
    x2, y2, z2 = coordinates2

    coord_dist = math.sqrt ((x2-x1)**2 + (y2 - y1)**2 + (z1 - z2)**2)

    return coord_dist

def main():
    try:
        coordinates1 = tuple(map(float, input("Enter the first coordinates(x y z): ").split()))
        coordinates2 = tuple(map(float, input("Enter the second coordinates(x y z): ").split()))
    except:
        print("Please try again and enter valid coordinates")


    coord_dist = distance(coordinates1, coordinates2)

    print(f"The distance between the two coordinates is: {coord_dist:0.2f}")

if __name__ == '__main__':
    main()

TestRun:
Enter the first coordinates(x y z): 3 7 6
Enter the second coordinates(x y z): 3 2 4
The distance between the two coordinates is: 5.39
