def get_type(x, y, width, height):
    if x >= width or y >= height:
        return 'invalid'
    if x == 0 and y == 0:
        return 'top_left'
    elif x == 0 and y == height-1:
        return 'bottom_left'
    elif x == width-1 and y == 0:
        return 'top_right'
    elif x == width-1 and y == height-1:
        return 'bottom_right'
    elif x == 0:
        return 'left_edge'
    elif x == width-1:
        return 'right_edge'
    elif y == 0:
        return 'top_edge'
    elif y == height-1:
        return 'bottom_edge'
    else:
        return 'box'


def get_max_size(x, y, width, height):
    node_type = get_type(x, y, width, height)
    if node_type in ['top_left', 'bottom_left', 'top_right', 'bottom_right']:
        return 2
    elif node_type in ['left_edge', 'right_edge', 'top_edge', 'bottom_edge']:
        return 3
    elif node_type in ['box']:
        return 4
    else:
        return 0


def get_adjacent_node_coordinates(type, x, y):
    if type == 'top_left':
        return [(1, 0), (0, 1)]
    elif type == 'top_right':
        return [(x - 1, 0), (x, 1)]
    elif type == 'bottom_left':
        return [(0, y - 1), (1, y)]
    elif type == 'bottom_right':
        return [(x - 1, y), (x, y - 1)]
    elif type == 'left_edge':
        return [(0, y - 1), (0, y + 1), (1, y)]
    elif type == 'right_edge':
        return [(x, y - 1), (x, y + 1), (x - 1, y)]
    elif type == 'top_edge':
        return [(x - 1, 0), (x + 1, 0), (x, 1)]
    elif type == 'bottom_edge':
        return [(x - 1, y), (x + 1, y), (x, y - 1)]
    elif type == 'box':
        return [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]


def get_nodes_from_coordinates(node_list, coordinates):
    nodes = []
    for c in coordinates:
        n = filter(lambda k: k.x == c[0] and k.y == c[1], node_list)
        nodes.extend(n)
    return nodes


class Node:

    def __init__(self, x, y, width, height, node_list):
        self.x = x
        self.y = y
        self.type = get_type(x, y, width, height)
        self.max_size = get_max_size(x, y, width, height)
        self.current_size = 0
        self.current_color = None
        self.node_list = node_list

    def add_no_turn(self, color):
        if self.current_color is None or self.current_color == color:
            self.current_color = color
            self.current_size += 1
            self.split_if_full()
            return True
        else:
            return False

    def capture(self, color):
        self.current_color = color
        self.current_size += 1

    def split_if_full(self):
        if self.current_size == self.max_size:
            node_coordinates = get_adjacent_node_coordinates(self.type, self.x, self.y)
            adjacent_nodes = get_nodes_from_coordinates(self.node_list, node_coordinates)
            for node in adjacent_nodes:
                node.capture(self.current_color)
            self.current_size = 0
            self.current_color = None
            for node in adjacent_nodes:
                node.split_if_full()