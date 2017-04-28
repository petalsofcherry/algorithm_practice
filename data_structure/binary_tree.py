#-*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class OperateTree(object):
    def pre_search(self, pRoot):
        if pRoot is None:
            return
        print(pRoot.val)
        self.pre_search(pRoot.left)
        self.pre_search(pRoot.right)

    def inorder_search(self, pRoot):
        if pRoot is None:
            return
        self.pre_search(pRoot.left)
        print(pRoot.val)
        self.pre_search(pRoot.right)

    def suff_search(self, pRoot):
        if pRoot is None:
            return
        self.pre_search(pRoot.left)
        self.pre_search(pRoot.right)
        print(pRoot.val)

    def floor_search(self, pRoot):
        if pRoot is None:
            return
        node = pRoot
        temp = [node]
        while temp:
            node = temp.pop(0)
            print(node.val)
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)

    def true_search(self, pRoot):
        # write code here
        if not pRoot:
            return []
        curr = [pRoot]
        curr_val = [pRoot.val]
        line = 1
        while curr:
            print(curr_val)
            print('\n')
            next_val = []
            next = []
            for node in curr:
                if node.left:
                    next.append(node.left)
                    next_val.append(node.left.val)
                else:
                    next_val.append('#')
                if node.right:
                    next.append(node.right)
                    next_val.append(node.right.val)
                else:
                    next_val.append('#')
                curr = next
                curr_val = next_val
            line += 1

    def find(self, pRoot, val):
        if val == pRoot.val:
            return pRoot
        elif val < pRoot.val and pRoot.left:
            return self.find(pRoot.left, val)
        elif val < pRoot.val and pRoot.right:
            return self.find(pRoot.right, val)
        else:
            return None

    def insert(self, pRoot, val):
        if val < pRoot.val:
            if pRoot.left:
                self.insert(pRoot.left, val)
            else:
                node = TreeNode(val)
                pRoot.left = node
        if val > pRoot.val:
            if pRoot.right:
                self.insert(pRoot.right, val)
            else:
                node = TreeNode(val)
                pRoot.right = node

    def del_node(self, pRoot, val):
        pass


if __name__ == '__main__':
    pRoot = TreeNode(22)
    test = OperateTree()
    for i in range(50):
        test.insert(pRoot, i)
    test.true_search(pRoot)
