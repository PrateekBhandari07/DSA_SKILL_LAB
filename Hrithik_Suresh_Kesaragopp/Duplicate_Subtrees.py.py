from collections import defaultdict

class TreeNode:
    def _init_(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_duplicate_subtrees(root):
    seen = defaultdict(int)
    result = []

    def traverse(node):
        if not node:
            return "#"
        structure = f"{node.val},{traverse(node.left)},{traverse(node.right)}"
        seen[structure] += 1
        if seen[structure] == 2:
            result.append(node)
        return structure

    traverse(root)
    return [node.val for node in result]

# Example Tree
root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(2, TreeNode(4)), TreeNode(4)))
print("Duplicate Subtrees:", find_duplicate_subtrees(root))