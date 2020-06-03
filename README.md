# MazeSolver
Implementation, Analysis and Comparison of Various maze solving algorithms.

Algorithms covered:
BFS, DFS, A Star, Dijkstra.


To run locally,
```bash
solve.py -m <methodname> <imagepath> 
```
method names = ["breadthfirst", "depthfirst", "dijksta", "astar"]

* The program takes as input a maze image where the image dimensions equals the maze dimensions.

* By default, breadthfirst is used as method.
* After execution, another image ending with _sol_methodname appended to your image name will be created as a solution.
Example, if your file was image.png, solution will be saved as image_sol_methodname.png
* The program  displays execution times of each process.
* It also creates a visual runtime graph, stored as profiler.png

