from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


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
# print('PLAYEERRRR!!', player.current_room)
# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# TASK: CONSTRUCT MY OWN TRAVERSAL GRAPH
# Start in room 0 which contains exits ['n', 's', 'w', 'e'].
# DONE TRAVERSING when there are exactly 500 entries in the graph and no '?' in the adjacency dictionaries - BASE CASE?
# This traversal algorithm logs the path into traversal_path. 

# I need to create a loop that:
    # Tried to move in a direction
    # If in a new room, fill in the entries in the graph, showing that the previous room has an exit that lead to the current room an vice versa.

    # Do this until all rooms have been visited and there are 500 entries in the graph with no '?' in the dictionary.

# Do a DFS for everything past '?' unitl it reaches a room with no unexplored paths (dead-end).
    # Add the rooms to the traversal path while going through them.
    # When hitting a dead-end, move back to the nearest room that contains an unexplored path. Until room with exit '?'.

# Use BFS to find the shortest path to an unexplored room. (Use code from earlier this week, but searching for the '?'). This will find the nearest room with '?' for exit
    # If an exit has been exlored, add it in BFS queue
    # Make sure to convert the path returned to a list of n/s/e/w directions before adding it to traversal path.


# CREATAE SEPARATE FUNCTIONS FOR BFS AND DFS

# 







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
