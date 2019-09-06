from queue import PriorityQueue

def gs(graph, initial, h):
    pqueue = PriorityQueue()
    visited = set()
    pqueue.put( (h(initial), initial, []))
    visited.add(str(initial))
    unqueued = 0
    while not pqueue.empty():
        priority,node,path = pqueue.get_nowait()
        unqueued += 1
        if priority == 0 :
            print("unqueued: %s, visited: %s" % (unqueued, len(visited)))
            return node,path
        for label,target_node in graph[node].items():
            key_target_node = str(target_node)
            if key_target_node not in visited:
                pqueue.put_nowait((
                    h(target_node),
                    target_node,
                    path + [label]
                ))
                visited.add(key_target_node)
    return None