def dls(tree, node, limit, depth=0, visited=None):
    if visited is None:
        visited = []

    # Visit the current node
    visited.append(node)

    # If depth limit reached, stop further expansion
    if depth == limit:
        return visited

    # Explore children
    for child in tree.get(node, []):
        if child not in visited:
            dls(tree, child, limit, depth + 1, visited)

    return visited


# Example tree
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Execution with depth limit = 2
print("DLS Traversal (limit = 2):", dls(tree, 'A', 2))
def dls_for_iddfs(tree, node, limit, depth=0, visited=None):
    if visited is None:
        visited = []

    visited.append(node)

    if depth == limit:
        return

    for child in tree.get(node, []):
        if child not in visited:
            dls_for_iddfs(tree, child, limit, depth + 1, visited)


def iddfs(tree, root, max_depth):
    for limit in range(max_depth + 1):
        visited = []
        dls_for_iddfs(tree, root, limit, 0, visited)
        print(f"Depth {limit}:", visited)


# Example tree
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Execution up to depth 3
iddfs(tree, 'A', 3)
