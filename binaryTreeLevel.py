class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree(node_map, node_val):
    if node_val not in node_map:
        return None

    node = Node(node_val)
    left_val, right_val = node_map[node_val]

    node.left = build_tree(node_map, left_val)
    node.right = build_tree(node_map, right_val)

    return node


def calculate_level(node):
    if node is None:
        return 0
    else:
        left_level = calculate_level(node.left)
        right_level = calculate_level(node.right)

        return max(left_level, right_level) + 1


# Leitura do arquivo tree.arv
node_map = {}
with open("tree.arv", "r") as file:
    for line in file:
        parent, children = line.strip().split(";")
        left, right = children.split(",")
        node_map[parent] = (left, right)

# Construção da árvore binária
root = build_tree(node_map, 'a')

# Cálculo do nível da árvore
level = calculate_level(root)

# Impressão do nível
print("O nível da árvore é:", level)
