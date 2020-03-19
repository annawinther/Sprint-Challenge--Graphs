from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
print('PLAYEERRRR!!', player.current_room.id)
print('EXITS!!', player.current_room.get_exits())

print('TRAVVELLLL!!', player.travel(['s']))


# TASK: CONSTRUCT MY OWN TRAVERSAL GRAPH
# Start in room 0 which contains exits ['n', 's', 'w', 'e'].
# DONE TRAVERSING when there are exactly 500 entries in the graph and no '?' in the adjacency dictionaries - BASE CASE?
# This traversal algorithm logs the path into traversal_path. 

# I need to create a loop that:
    # Tried to move in a direction
    # If in a new room, fill in the entries in the graph, showing that the previous room has an exit that lead to the current room an vice versa.

    # Do this until all rooms have been visited and there are 500 entries in the graph with no '?' in the dictionary.

# Use BFS to find the shortest path to an unexplored room. (Use code from earlier this week, but searching for the '?'). This will find the nearest room with '?' for exit
    # If an exit has been exlored, add it in BFS queue
    # Make sure to convert the path returned to a list of n/s/e/w directions before adding it to traversal path.

# Do a DFS for everything past '?' unitl it reaches a room with no unexplored paths (dead-end).
    # Add the rooms to the traversal path while going through them.
    # When hitting a dead-end, move back to the nearest room that contains an unexplored path. Until room with exit '?'.



# CREATAE SEPARATE FUNCTIONS FOR BFS AND DFT

# start at player.current_room

# loop over using dft until there is a dead-end
    # on every move a new direction, add the room to traverse path and mark visited

    # when hitting a dead end
        # do a BFS to find the shortest path to an unvistied room 
        # save the path on every move to that new room and run the path with the player in order to get to the room

# then repeat a dft until reaching the next dead-end and repeat bfs to find the next shortest path

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

def dft(player):
    """
    Print each vertex in depth-first order
    beginning from starting_vertex.
    """
    # create an empty stack, push the starting vertex index
    s = Stack()
    s.push(player.current_room.id)
    # create a set to store the visited vertices
    visited = []
    # while stack is not empty (len greater than 0)
    while s.size() > 0:
        # pop the first vertex
        current_room = s.pop()
        # if that vertex has not been visitied 
        if current_room not in visited:
            # mark as visited and print for debugging
            visited.append(current_room)
            print(current_room)
            # iterate through the child vertices of the current vertex
            for next_vertex in current_room.get_exits():
                # push the next vertex
                s.push(next_vertex)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
