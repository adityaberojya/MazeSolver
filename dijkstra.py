from FibonacciHeap import FibHeap
from priority_queue import FibPQ, HeapPQ, QueuePQ

def solve(maze):
    width = maze.width
    total = maze.width * maze.height

    start = maze.start
    startpos = start.Position
    end = maze.end
    endpos = end.Position

    visited = [False] * total

    prev = [None] * total

    infinity = float("inf")
    distances = [infinity] * total

    # You can change what kind of priority queues you wish to use.
    
    # unvisited = FibHeap()
    unvisited = HeapPQ()
    # unvisited = FibPQ()
    # unvisited = QueuePQ()

    nodeindex = [None] * total
    distances[start.Position[0] * width + start.Position[1]] = 0
    startnode = FibHeap.Node(0, start)
    nodeindex[start.Position[0] * width + start.Position[1]] = startnode
    unvisited.insert(startnode)

    count = 0
    completed = False

    # Begin Dijkstra - continue while there are unvisited nodes in the queue
    while len(unvisited) > 0:
        count += 1

        # Find current shortest path point to explore
        n = unvisited.removeminimum()

        u = n.value
        upos = u.Position
        uposindex = upos[0] * width + upos[1]

        if distances[uposindex] == infinity:
            break

        if upos == endpos:
            completed = True
            break

        for v in u.Neighbours:
            if v != None:
                vpos = v.Position
                vposindex = vpos[0] * width + vpos[1]

                if visited[vposindex] == False:
                    d = abs(vpos[0] - upos[0]) + abs(vpos[1] - upos[1])

                    newdistance = distances[uposindex] + d

                    if newdistance < distances[vposindex]:
                        vnode = nodeindex[vposindex]
                        # v isn't already in the priority queue - add it
                        if vnode == None:
                            vnode = FibHeap.Node(newdistance, v)
                            unvisited.insert(vnode)
                            nodeindex[vposindex] = vnode
                            distances[vposindex] = newdistance
                            prev[vposindex] = u
                        # v is already in the queue - decrease its key to re-prioritise it
                        else:
                            unvisited.decreasekey(vnode, newdistance)
                            distances[vposindex] = newdistance
                            prev[vposindex] = u

        visited[uposindex] = True

    from collections import deque

    path = deque()
    current = end
    while (current != None):
        path.appendleft(current)
        current = prev[current.Position[0] * width + current.Position[1]]

    return [path, [count, len(path), completed]]
