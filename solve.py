from PIL import Image
import time
from mazes import Maze
import bprofile

# Read command line arguments - the python argparse class is convenient here.
import argparse

def solve(method, input_file):
    # Load Image
    print ("Loading Image")
    im = Image.open(input_file)

    # Create the maze (and time it) - for many mazes this is more time consuming than solving the maze
    print ("Creating Maze")
    t0 = time.time()
    maze = Maze(im)
    t1 = time.time()
    print ("Node Count:", maze.count)
    total = t1-t0
    print ("Time elapsed:", total)

    # Create and run solver
    [title, solver] = getSolver(method)
    print ("Starting Solve:", title, " on image ", input_file)

    t0 = time.time()
    [result, stats] = solver(maze)
    t1 = time.time()

    total = t1-t0

    # Print solve stats
    print ("Nodes explored: ", stats[0])
    if (stats[2]):
        print ("Path found, length", stats[1])
    else:
        print ("No Path Found")
    print ("Time elapsed: ", total)

    print ("Saving Image\n")
    im = im.convert('RGB')
    impixels = im.load()

    resultpath = [n.Position for n in result]

    length = len(resultpath)

    for i in range(0, length - 1):
        a = resultpath[i]
        b = resultpath[i+1]

        # Blue - red
        r = int((i / length) * 255)
        px = (r, 0, 255 - r)

        if a[0] == b[0]:
            # Ys equal - horizontal line
            for x in range(min(a[1],b[1]), max(a[1],b[1])):
                impixels[x,a[0]] = px
        elif a[1] == b[1]:
            # Xs equal - vertical line
            for y in range(min(a[0],b[0]), max(a[0],b[0]) + 1):
                impixels[a[1],y] = px


    im.save( input_file[:-4] +"_sol_"+ method +".png")

profiler = bprofile.BProfile('profiler.png')

def getSolver(method):
    if method == "depthfirst":
        import depthfirst
        return ["Depth first search", depthfirst.solve]
    elif method == "dijkstra":
        import dijkstra
        return ["Dijkstra's Algorithm", dijkstra.solve]
    elif method == "astar":
        import astar
        return ["A-star Search", astar.solve]
    else :
        import breadthfirst
        return ["Breadth first search", breadthfirst.solve]


def main():
    Default = "breadthfirst"
    Choices = ["breadthfirst","depthfirst","dijkstra", "astar"]
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-m", "--method", nargs='?', const=Default, default=Default, choices=Choices)
    parser.add_argument("input_file")

    args = parser.parse_args()

    # The profiler generator a visual graph of the program during its execution.
    with profiler:
        solve(args.method, args.input_file)

if __name__ == "__main__":
    main()

