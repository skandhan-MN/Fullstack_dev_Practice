class Solution:
    def preorder(self, root):
        if not root:
            return []

        tree = [root.val]
        if root.children:
            for child in root.children:
                tree += self.preorder(child)
        return tree


if __name__ == "__main__":

    Solution()
