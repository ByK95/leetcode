from typing import Optional, List

class Test:
    @staticmethod
    def load_from_file(filename):
        with open(f"./{filename}", 'r') as f:
            return f.read()

    @classmethod
    def run(cls):
        instance = cls()
        methods = [method for method in dir(instance) if method.startswith('test')]
        for method in methods:
            func = getattr(instance, method)
            func()

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(Test):
    def test_sample(self):
        a = TreeNode(7)
        b = TreeNode(15)
        c = TreeNode(20, b, a)
        d = TreeNode(9)
        root = TreeNode(3, d, c)

        result = self.zigzagLevelOrder(root)
        print(result)

    def test_sample_2(self):
        a = TreeNode(1)

        result = self.zigzagLevelOrder(a)
        print(result)

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        values = []

        if not root:
            return values

        nodes_to_visit = [(0, root)]
        
        while len(nodes_to_visit) > 0:
            depth, node = nodes_to_visit.pop()
            if len(values) == depth:
                values.append([node.val])
            else:
                values[depth].append(node.val)

            if node and node.right != None:
                nodes_to_visit.append((depth+1 ,node.right))

            if node and node.left != None:
                nodes_to_visit.append((depth+1 ,node.left))

        for odd in range(1, len(values), 2):
            values[odd].reverse()

        return values


if __name__ == '__main__':
    Solution.run()