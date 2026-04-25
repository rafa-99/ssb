class TreeNode:
    def __init__(self, name, children=None):
        self.name = name
        self.children = children or []
        self.checked = False
        self.expanded = False


def build_model(data):
    if isinstance(data, dict):
        return [TreeNode(k, build_model(v)) for k, v in data.items()]
    return []


def set_children(node, state):
    for child in node.children:
        child.checked = state
        set_children(child, state)


def get_selected_paths(node, path=()):
    results = []

    current_path = path + (node.name,)

    if node.checked:
        results.append(current_path)

    for child in node.children:
        results.extend(get_selected_paths(child, current_path))

    return results