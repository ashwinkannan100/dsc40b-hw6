import dsc40graph
from collections import deque

def assign_good_and_evil(graph):
    '''
    Assigns good and evil labels to nodes in a graph.
    '''
    # TODO: Implement the assign_good_and_evil function

    pending = deque()
    
    status = {}

    for node in graph.nodes:
        status[node] = ' '
    
    for node in graph.nodes:

        if status[node]==' ':
            status[node] = 'good'
            pending.append(node)
            
            while pending:
                u = pending.popleft()
                for v in graph.neighbors(u):
                    if status[u] == 'good':
                        if status[v]== ' ':
                            pending.append(v)
                            status[v] = 'evil'
                        elif status[v] == 'good':
                            return None
                    elif status[u] == 'evil':
                        if status[v]== ' ':
                            pending.append(v)
                            status[v] = 'good'
                        elif status[v] == 'evil':
                            return None
            
                
    return status
