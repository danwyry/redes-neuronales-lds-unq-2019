import timeit
from collections import deque

FORTH, BACK = 1, -1   # Sentidos
FARMER, WOLF, GOAT, CABBAGE = 1,2,4,8   # Caracteres
IMPOSSIBLE_COMBINATIONS = [WOLF + GOAT, GOAT + CABBAGE]

def node_possible_moves(node):
    moves = []
    A,B = node
    sense = FORTH if (A%2==1) else BACK
    for ch in [0, WOLF, GOAT, CABBAGE]:
        if ((B if sense==FORTH else A) & ch) == 0:
            moves.append((ch,sense))
    return moves

def is_goal_node(node):
    return node[0] == 0 and node[1] == 15

def is_loosing_node(node):
    A,B = node
    return A in IMPOSSIBLE_COMBINATIONS or B in IMPOSSIBLE_COMBINATIONS

def apply_move(node, edge):
    A,B = node
    character, sense = edge
    if sense == FORTH:
        A -= (FARMER + character)
        B += FARMER + character
    else: 
        A += FARMER + character
        B -= (FARMER + character)
    return (A,B)

def is_valid_move(node, move):
    A,B = node
    _,sense = move
    return  sense==FORTH and A % 2 == 1 or sense==BACK and B % 2 == 1

def build_game_graph():
    """
    :return: Dupla ([Nodo],[Eje]) donde cada Nodo es una dupla de enteros representando la suma de los caracteres
    contenidos de un lado y del otro del río, y la lista de ejes es una lista que se asocia uno a uno por el índice a la
    lista de nodos, y contiene la lista de los nodos adyacentes a cada uno
    """
    node_list = [ (15, 0) ] # INITIAL NODE
    nodes_edges = []
    i=0
    while i < len(node_list):
        node = node_list[i]
        node_adjacents = []
        if not is_goal_node(node) and not is_loosing_node(node):
            for move in node_possible_moves(node):
                adj_node = apply_move(node, move)
                node_adjacents.append(adj_node)
                if adj_node not in node_list:
                    node_list.append(adj_node)
        nodes_edges.append(node_adjacents)
        i+=1
    i = 0
    graph = {}
    for i in range(len(node_list)): graph.update({node_list[i]: nodes_edges[i]})
    return graph

print("Time algo ad-hoc: " , timeit.timeit(build_game_graph,number=100))
graph1 = build_game_graph()

for n in graph1: print (n,graph1[n])

def bfs(graph, initial, is_goal):
    visited = set()
    stack = deque( [ (initial,[]) ] )
    while stack:
        node,path = stack.pop()
        if is_goal(node):
            return node,path
        adjacents = graph[node]
        for adj in adjacents:
            # if is_loosing_node(adj): continue
            if adj not in visited:
                stack.append( (adj, path + [adj]) )
                visited.add(adj)
    return None

def dfs(graph, initial, is_goal):
    visited = set()
    queue = deque( [ (initial,[]) ] )
    while queue:
        node,path = queue.popleft()
        if is_goal(node):
            return node,path
        adjacents = graph[node]
        for adj in adjacents:
            # if is_loosing_node(adj): continue
            if adj not in visited:
                queue.append( (adj, path + [adj]) )
                visited.add(adj)
    return None

def test1():
    global graph1
    _ = bfs(graph1, (15, 0), is_goal_node)

def test2():
    global graph1
    _ = dfs(graph1, (15, 0), is_goal_node)

print("Time algo BFS: " , timeit.timeit(test1,number=10000))
print("Time algo DFS: " , timeit.timeit(test2,number=10000))

print ("BFS: ", bfs(graph1, (15, 0), is_goal_node))
print ("DFS: ", dfs(graph1, (15, 0), is_goal_node))