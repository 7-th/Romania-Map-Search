import heapq

Map = {
    'Arad' : {'Zerind' : 75, 'Sibiu': 140, 'Timisoara' : 118},
    'Zerind' : {'Arad': 75, 'Oradea': 71},
    'Oradea' : {'Zerind' : 71, 'Sibiu' : 151},
    'Timisoara' : {'Arad' : 118, 'Lugoj': 111},
    'Lugoj' : {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia' : {'Lugoj': 70 , 'Dobreta': 75},
    'Dobreta' : {'Mehadia': 75, 'Craiova': 120},
    'Craiova' : {'Dobreta':120, 'Rimnicu': 146, 'Pitesti': 138},
    'Rimnicu' : {'Sibiu' : 80, 'Craiova': 146, 'Pitesti': 97},
    'Sibiu' : {'Rimnicu' : 80, 'Fagaras': 99, 'Arad': 140, 'Oradea': 151},
    'Fagaras' : {'Sibiu' : 99, 'Bucharest': 211 },
    'Pitesti' : {'Rimnicu' : 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest' : {'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Urziceni' : {'Hirsova' : 98, 'Bucharest' : 85, 'Vaslui': 142},
    'Giurgiu' : {'Bucharest' : 90},
    'Hirsova' : {'Urziceni' : 98, 'Eforie': 86},
    'Eforie' : {'Hirsova' : 86 },
    'Vaslui' : {'Urziceni' : 142, 'Iasi' : 92},
    'Iasi' : {'Vaslui': 92, 'Neamt': 87},
    'Neamt' : {'Iasi': 87}
}

###########################################################################################################################################
############################################### Uninformed Search Algorithms  #############################################################
###########################################################################################################################################

# (BFS) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def BFS_breadth_first_search(start, goal, graph=Map):
    visited = [] # Explored set
    queue = [(start, [start])] # fronter

    while queue:
        cost = 0
        current_node, path = queue.pop(0)

        if current_node == goal:
            for i in range(len(path)-1):
                cost += graph[path[i]][path[i+1]]
            return (path, cost) # Return to the GUI

        visited.append(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited :
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))

    return ("False", "False")  # If the goal is not reached

# (DLS) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def DLS_depth_limited_search(start, goal, depth_limit:int=3, graph=Map):

    stack = [(start, [start], 0)]
    visited = []

    cost = 0
    while stack:
        current_node, path, depth = stack.pop()
        if current_node == goal:
            for i in range(len(path)-1):
                cost += graph[path[i]][path[i+1]]

            return (path, cost) # Return to the GUI

        if depth < depth_limit:

            if current_node in visited:
              continue

            visited.append(current_node)
            for neighbor in reversed(graph[current_node]):
              if neighbor not in visited :
                stack.append((neighbor, path + [neighbor], depth + 1))

    return ("False", "False")  # If the goal is not reached

# (DFS) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def DFS_depth_first_search(start, goal, graph=Map):
    visited = [] # Explored set
    stack = [(start, [start])] # fronter

    while stack:
        cost = 0
        current_node, path = stack.pop()

        if current_node == goal:
            for i in range(len(path)-1):
                cost += graph[path[i]][path[i+1]]
            return (path, cost) # Return to the GUI

        visited.append(current_node)


        for neighbor in reversed(graph[current_node]):
            if neighbor not in visited :
              stack.append((neighbor, path + [neighbor]))

    return ("False", "False")  # If the goal is not reached

# (UCS) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def UCS_uniform_cost_search(start, goal, graph=Map): # Using heapq for priority queue
    
    import heapq

    priority_queue = [(0, start, [])]  # Each element is a tuple (cost, node, path)
    visited = []

    while priority_queue:
        current_cost, current_node, path_so_far = heapq.heappop(priority_queue)

        if current_node == goal:
            return ((path_so_far + [current_node]), current_cost)  # Return cost and path

        if current_node in visited:
            continue

        visited.append(current_node)

        for neighbor, cost in graph[current_node].items():
            if neighbor not in visited:
                total_cost = current_cost + cost
                heapq.heappush(priority_queue, (total_cost, neighbor, path_so_far + [current_node]))

    return ("False", "False")  # If the goal is not reached

# (IDDFS) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def IDDFS_iterative_deepening_depth_first_search(start, goal, graph=Map):
    for depth in range(100):
        result = DLS_depth_limited_search(start, goal, depth, graph)
        if result[0] != "False":
            return result

    return ("False", "False")  # If the goal is not reached

# (Bidirectional search) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def Bidirectional_search(start, goal, graph=Map):

    forward_queue = [(start, [start])]  # Queue for the forward search
    backward_queue = [(goal, [goal])]    # Queue for the backward search

    visited_start = []  # Set to keep track of visited nodes in the forward search
    visited_goal = []  # Set to keep track of visited nodes in the backward search

    # Initialize path lists for forward and backward search
    forward_paths = {start: [start]}
    backward_paths = {goal: [goal]}

    while forward_queue and backward_queue:

    # Forward search ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        current_start, path_start = forward_queue.pop(0)
        visited_start.append(current_start)

        if current_start in visited_goal:
            cost = 0
            backward_path = backward_paths[current_start]
            backward_path.pop()
        # Calculate the cost of the path
            for i in range(len(path_start)-1):
                cost += graph[path_start[i]][path_start[i+1]]

            return ((forward_paths[current_start] + backward_path[::-1]), cost)


        for neighbor in graph[current_start]:
            if neighbor not in visited_start:
                forward_queue.append((neighbor, path_start + [neighbor]))
                forward_paths[neighbor] = path_start + [neighbor]

    # Backward search ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        current_goal, path_goal = backward_queue.pop(0)
        visited_goal.append(current_goal)

        if current_goal in visited_start:
            cost = 0

            forward_path = forward_paths[current_goal]
            forward_path.pop()
            # Calculate the cost of the path
            for i in range(len(path_goal)-1):
                cost += graph[path_goal[i]][path_goal[i+1]]

            return ((forward_path + backward_paths[current_goal][::-1]), cost)

        for neighbor in graph[current_goal]:
            if neighbor not in visited_goal:
                backward_queue.append((neighbor, path_goal + [neighbor]))
                backward_paths[neighbor] =  path_goal + [neighbor]

    return ("False", "False")  # If the goal is not reached

#########################################################################################################################################
############################################### Informed Search Algorithms  #############################################################
#########################################################################################################################################

heuristic_values = {
    'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Dobreta': 242, 'Zerind' : 80, 
    'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 
    'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234, 
    'Oradea': 380, 'Pitesti': 100, 'Rimnicu': 193, 'Sibiu': 253, 
    'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Iasi': 226
    }

# (Greedy Algorithm) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def Greedy_Algorithm(start, goal, graph=Map):

    # Priority queue with (heuristic value, node, path) tuples
    queue = [(heuristic_values[start], start, [start])]

    visited = set()

    cost = 0
    while queue:
        _, node, path = queue.pop(0)  # Get the node with the lowest heuristic value

        if node == goal:
            for i in range(len(path)-1):
                cost += graph[path[i]][path[i+1]]

            return (path, cost)  # Return the path from start to goal

        visited.add(node)

        if node in graph:
            neighbors = graph[node]
            for neighbor in neighbors:
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    queue.append((heuristic_values[neighbor], neighbor, new_path))

        queue.sort()  # Sort the queue based on heuristic value

    return ("False", "False")  # If the goal is not reached

# (A* Algorithm) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def A_Star_Algorithm(start, goal, graph=Map):

    # Priority queue with (heuristic_value, node, path) tuples
    queue = [(0, start, [start])]

    visited = []

    final_cost = 0

    while queue:
        # Get the node with the lowest heuristic value
        cost, node, path = heapq.heappop(queue)

        if node == goal:
            for i in range(len(path)-1):
                final_cost += graph[path[i]][path[i+1]]

            return (path, final_cost)  # Return the path from start to goal

        visited.append(node)

        if node in graph:
            neighbors = graph[node]

            for neighbor, eage_cost in neighbors.items():

                if neighbor not in visited:
                    new_path = path + [neighbor]
                    new_cost = cost + eage_cost

                    total_cost = new_cost + heuristic_values[neighbor]

                    heapq.heappush(queue, (total_cost, neighbor, new_path))

    return ("False", "False")  # If the goal is not reached

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
