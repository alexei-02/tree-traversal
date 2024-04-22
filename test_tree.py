import unittest
from tree import Node, Tree

class TestTree(unittest.TestCase):
    def setUp(self):
        # Create a sample tree for testing
        self.node1 = Node(5)
        self.tree = Tree()
        self.node2 = Node(3)
        self.node3 = Node(7)
        self.node1.left = self.node2
        self.node1.right = self.node3

    def test_find_equal(self):
        result = self.tree._find(5, self.node1)
        self.assertEqual(result, self.node1)

    def test_find_less_than(self):
        result = self.tree._find(3, self.node1)
        self.assertEqual(result, self.node2)

    def test_find_greater_than(self):
        result = self.tree._find(7, self.node1)
        self.assertEqual(result, self.node3)

    def test_find_less_than_none(self):
        result = self.tree._find(2, self.node1)
        self.assertIsNone(result)

    def test_find_greater_than_none(self):
        result = self.tree._find(8, self.node1)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()