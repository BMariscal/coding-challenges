"""
In a multithreaded environment, it's possible that different processes will need to use the same resource.
A wait-for graph represents the different processes as nodes in a directed graph, where an edge from node i to node j
means that the node j is using a resource that node i needs to use (and cannot use until node j releases it).

We are interested in whether or not this digraph has any cycles in it. If it does, it is possible for the system to
get into a state where no process can complete.

We will represent the processes by integers 0, ...., n - 1. We represent the edges using a two-dimensional list connections.
If j is in the list connections[i], then there is a directed edge from process i to process j.

Write a function that returns True if connections describes a graph with a directed cycle, or False otherwise.



For connections = [[1], [2], [3, 4], [4], [0]], the output should be
hasDeadlock(connections) = true. # has cycle

For connections = [[1, 2, 3], [2, 3], [3], []], the output should be
hasDeadlock(connections) = false.



Deadlock presents in a system if and only if we encounter a cycle in the Wait-for graph.
Then, every transaction which is part of the cycle in the Wait-for graph will be treated as in the deadlock state.
To detect this, the system has to employ the algorithm which checks the Wait-for graph for possible deadlock periodically.
The Wait-for graph given in the Figure 1, has formed a cycle.
That is, T1 is waiting for the resource held by T2 and T2 in turn waiting for resources held by T1.
This deadlock situation need not involve all the transactions that are happening in a time.
It may involve some of the transactions that are part of Wait-for graph at that moment as given
http://www.exploredatabase.com/2014/04/deadlock-detection-technique-in-database.html
https://www.youtube.com/watch?v=a7UGIqR0cI0
"""


def hasDeadlock(connections):
    visited = [False] * len(connections)
    stack = [False] * len(connections)

    for node in range(len(connections)):
        if visited[node] == False:
            if DFS(connections, node, visited, stack) == True:
                return True
    return False


def DFS(adj, node, visited, stack):
    visited[node] = True
    stack[node] = True

    for w in adj[node]:
        if visited[w] == False:
            if DFS(adj, w, visited, stack) == True:
                return True
        elif stack[w] == True:
            return True
    stack[node] = False
    return False

