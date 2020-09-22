"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # left?
        # check if the value is less than the root
        if value < self.value:
            # move to the left and check if it is None
            if self.left is None:
                # insert node here
                self.left = BSTNode(value)
            # otherwise
            else:
                # call insert on the root's left node
                self.left.insert(value)
        # right?
        # check if the value is greater than the root
        else:
            # move to the right and check if it is None
            if self.right is None:
                # insert node here
                self.right = BSTNode(value)
            else:
                # call insert on the root's right node
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # check if self.value is target
        if self.value is target:
            # if yes, return True
            return True
        # left?
        # check if the target is less than the root
        if target < self.value:
            # check if there's no child to the left
            if not self.left:
                return False
            else:
                # call contains on left child
                self.left.contains(target)
        # right?
        else:
            # check if there's no child to the right
            if not self.right:
                return False
            else:
                # call contains on the right child
                self.right.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        # check if tree is empty
        if self is None:
            return None

        # go right until you cannot anymore
        while self.right:
            self = self.right

        # return value at far right
        return self.value

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        # call for each on the root
        fn(self.value)

        # if left
        if self.left:
            # call for each on the left child
            self.left.for_each(fn)

        # if right
        if self.right:
            # call for each on the right child
            self.right.for_each(fn)
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()
