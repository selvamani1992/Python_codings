# This challenge deals with finding and counting the number of paths between points on a rectilinear grid. A starting point (x, y) with non-negative integer coordinates is provided. You are only allowed to move horizontally and vertically along the grid Hence, from (x, y) you may move to (x+1, y), (x-1, y). (x, y+1), or (x, y-1). Your goal is to return to the origin (0, 0) in such a way that you never increase the distance to the origin. The distance is counted as the minimum number of total vertical and horizontal steps to reach the origin

# Create a function that reads a starting location, (x, y) and returns the total number of different paths back to the origin Two paths are different if there is at least one step on the path that is different even if most of the steps are the same.

# x and y will always be integers greater than or equal to 0

# sample input
# 2 2

# sample output
# 6

def rectilinear_Paths(n, m):
    if (n == 0 or m == 0):
        return 1

    return (rectilinear_Paths(n - 1, m) +
            rectilinear_Paths(n, m - 1))

n, m = map(int,input().split())
total_path = rectilinear_Paths(n, m)
print(total_path)

# This code is contributed by ash264
