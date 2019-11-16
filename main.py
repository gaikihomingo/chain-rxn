from Node import Node
width = 5
height = 5

def print_grid(node_list, width):
    grid = [node_list[i:i + width] for i in range(0, len(node_list), width)]
    for line in grid:
        l = list(map(lambda n: {'size': n.current_size, 'color': n.current_color}, line))
        print(l)

def is_game_over(node_list):
    reds = list(filter(lambda n: n.current_color == 'red', node_list))
    greens = list(filter(lambda n: n.current_color == 'green', node_list))
    if len(reds) == 1 and len(greens) == 0 or len(greens) == 1 and len(reds) == 0:
        print("Game begins")
        return False
    elif len(reds) == 0:
        print("Green wins")
        return True
    elif len(greens) == 0:
        print("Red wins")
        return True
    else:
        print("Game on")
        return False

node_list = []
for i in range(width):
    for j in range(height):
        n = Node(i, j, width-1, height-1, node_list)
        node_list.append(n)

current = True
is_game_on = True
while(is_game_on):
    colors = ["red", "green"]
    color = colors[0] if current else colors[1]
    x = input("Grid number: ")
    if node_list[int(x)].add_no_turn(color):
        current = not current
        print_grid(node_list, width)
    else:
        print("Incorrect input. try other number")
    is_game_on = not is_game_over(node_list)
# print(len(node_list))
# print_grid(node_list, width)
#
# node_list[0].add_no_turn('red')
# node_list[1].add_no_turn('green')
# node_list[5].add_no_turn('red')
# node_list[6].add_no_turn('green')
# node_list[2].add_no_turn('red')
# node_list[6].add_no_turn('green')
# node_list[3].add_no_turn('red')
# node_list[6].add_no_turn('green')
# print("after play")
# print_grid(node_list, width)
# node_list[4].add_no_turn('red')
# node_list[6].add_no_turn('green')
# node_list[0].add_no_turn('red')
# node_list[13].add_no_turn('green')
# node_list[14].add_no_turn('red')
# node_list[15].add_no_turn('green')
# node_list[16].add_no_turn('red')
# node_list[17].add_no_turn('green')
# print("after play")
# print_grid(node_list, width)




