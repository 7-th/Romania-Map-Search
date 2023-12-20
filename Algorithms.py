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


# BFS:
def breadth_first_search(start, goal, graph = Map):
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