class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def find(self, data: int) -> TreeNode:
        curr = self.root
        while curr:
            if curr.val < data:
                curr = curr.right
            elif curr.val > data:
                curr = curr.left
            else:
                return curr
        return None

    def insert(self, data: int):
        if not self.root:
            self.root = TreeNode(data)
            return
        curr = self.root
        while curr:
            if curr.val < data:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = TreeNode(data)
                    break
            if curr.val > data:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = TreeNode(data)
                    break

    def findMin(self) -> int:
        if not self.root:
            return None
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr.val

    def findMax(self) -> int:
        if not self.root:
            return None
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.val

    def delete(self, data: int):
        pp = None
        curr = self.root
        while curr:
            if curr.val == data:
                break
            elif curr.val < data:
                pp = curr
                curr = curr.right
            else:
                pp = curr
                curr = curr.left

        if not curr:
            return

        if not curr.left and not curr.right:
            if not pp:
                root = None
            elif pp.left and pp.left.val == data:
                pp.left = None
            else:
                pp.right = None
            return

        if not curr.left:
            if not pp:
                root = curr.right
            elif pp.left and pp.left.val == data:
                pp.left = curr.right
            else:
                pp.right = curr.right
            return

        if not curr.right:
            if not pp:
                root = curr.left
            elif pp.left and pp.left.val == data:
                pp.left = curr.left
            else:
                pp.right = curr.left
            return

        # find minimum node in right hand side
        dummy = curr
        right = curr.right
        while right.left:
            dummy = right
            right = right.left

        if dummy.left == right:
            dummy.left = right.right
        else:
            dummy.right = right.right
        curr.val = right.val


BST = BinarySearchTree()
BST.insert(15)
BST.insert(21)
BST.insert(3)
print(BST.findMax())
BST.delete(3)
print(BST.findMin())
