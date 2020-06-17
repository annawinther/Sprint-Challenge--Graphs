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
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
# print('PLAYEERRRR!!', player.current_room.id)
# print('EXITS!!', player.current_room.get_exits())

# print('TRAVVELLLL!!', player.travel(['s']))


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

# start at player.current_room.id

# loop over using dft until there is a dead-end
    # on every move a new direction, add the room to traverse path and mark visited

    # when hitting a dead end
        # do a BFS to find the shortest path to an unvistied room 
        # save the path on every move to that new room and run the path with the player in order to get to the room

# then repeat a dft until reaching the next dead-end and repeat bfs to find the next shortest path

traversal_path = []
direction_pairs = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}

room_graph = {}

# refactor to use helper funcitons

# function to set the all exits for the current room
def set_exits(room):
    # assign the room key to an empty dict
    room_graph[room] = {}
    # loop over all exits of the current room 
    for exit in player.current_room.get_exits():
        # create a key in the room for all directions and assign '?'
        room_graph[room][exit] = '?'

# connect rooms connects the current room with the previous room 
def connect_rooms(previous_room, current_room, direction):
    # if the key does not exist 
    if not room_graph.get(current_room):
        # set it using our set_exits helper function
        set_exits(current_room)
    # set the directions to connect to the 2 rooms in apposing directions
    room_graph[previous_room][direction] = current_room
    room_graph[current_room][direction_pairs[direction]] = previous_room

# this returns a list of the unexplored exits for a room 
def unexplored(room):
    # create a dict of unexplored exits for that room
    unexplored_exits = []
    # loop over each exit of the extis to the current roo,
    for exit in player.current_room.get_exits():
        # if the exit is unexplored (has a '?')
        if room_graph[room][exit] == '?':
            # append exit to the dict
            unexplored_exits.append(exit)
    # return the dict of unexplored exits
    return unexplored_exits

# start with the first room and set exits for this room 
set_exits(player.current_room.id)
# set the first previous room to be the current room player is at
previous_room = player.current_room.id

# then to keep track of our route, use Stack and push the starting room to it
route = Stack()
route.push(player.current_room)

# loop over until we've visited all of the rooms (len of our room graph is smaller than the len of room sin the world)
while len(room_graph) < len(world.rooms):
    # if the previous room is in unexplored
    if unexplored(previous_room):
        # get the last exit from the stack and assing it to the move
        move = (unexplored(previous_room)).pop()
        # push that move onto our stack
        route.push(move)
    # otherwise
    else:
        # set the move to go the other way
        move = direction_pairs[route.pop()]
        print('MOVE', move)
    
    print('-' * 20)
    player.travel(move)
    print(f'you were in room {previous_room}')
    print(f'you are in room {player.current_room.id}')
    # print(player.current_room.get_exits())

    traversal_path.append(move)
    connect_rooms(previous_room, player.current_room.id, move)
    previous_room = player.current_room.id
    # print('-' * 20)



# def bfs(player, room_queue):
#     # get player current room id
#     current_rooms = rooms[player.current_room.id]
#     # store unexplored rooms
#     unexplored_rooms = []
#     # Loop over current room
#     for room in current_rooms:
#         # check if room direction is ?
#         if current_rooms[room] == '?':
#             # add to unexplored rooms
#             unexplored_rooms.append(room)
#     # check if the length is greater than 0
#     if len(unexplored_rooms) > 0:
#         # if it is add the first item to the queue
#         room_queue.enqueue(unexplored_rooms[0])
#     # otherwise
#     else:
#         # save the shortest unexplored path in a variable using our helper funciton 
#         unexplored_path = find_shortest_path(player, room_queue)

#         current_path = player.current_room.id
#         # loop over each path in our unexplored variable and each item in the rooms at the current path 
#         for path in unexplored_path:
#             for i in rooms[current_path]:
#                 # if equal to the path store it in the queue and update the current path
#                 if rooms[current_path][i] == path:
#                     room_queue.enqueue(i)
#                     current_path = path
#                     break

# def find_shortest_path(player, room_queue):
#     q = Queue()
#     # create a set to store the visited vertices
#     visited = set()
#     q.enqueue([player.current_room.id])
#     # while queue is not empty (len greater than 0)
#     while q.size() > 0:
#         room = q.dequeue()
#         last_path = room[-1]
#         # if this last path is not in visited, add it
#         if last_path not in visited:
#             visited.add(last_path)
#             # loop over all of the exits acosiated with the room
#             for exit in rooms[last_path]:
#                 # check to see if the exit at that room is equal to ? (unvisited)
#                 if rooms[last_path][exit] == '?':
#                     # if so, return the room
#                     return room
#                 else:
#                     # copy the path that we used in order to get to this exit for this room
#                     new_path = list(room)
#                     # append the next vertex accosiated with the exit to the new path
#                     new_path.append(rooms[last_path][exit])
#                     # Store the list in the Queue and reloop
#                     q.enqueue(new_path)
#     return []


# # TRAVERSAL TEST
# # traversal_path = []
# rooms = {}
# current_room = {}

# for exit in player.current_room.get_exits():
#         current_room[exit] = '?'
# rooms[player.current_room.id] = current_room

# room_queue = Queue()

# bfs(player, room_queue)

# while room_queue.size() > 0:
#     start_room = player.current_room.id
#     # print('start', start_room)
#     next_move = room_queue.dequeue()
#     # print('next', next_move)

#     player.travel(next_move)
#     traversal_path.append(next_move)

#     last_room = player.current_room.id
#     rooms[start_room][next_move] = last_room

#     if last_room not in rooms:
#         rooms[last_room] = {}

#         for direction in player.current_room.get_exits():
#             rooms[last_room][direction] = '?'

#     rooms[last_room][direction_pairs[next_move]] = start_room

#     if room_queue.size() == 0:
#         bfs(player, room_queue)

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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
