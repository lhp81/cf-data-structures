import unittest
from bst import BSTree


class TestingTheBasics(unittest.TestCase):
    """To make sure the basic parts of this work."""
    def setUp(self):
        self.my_bst = BSTree()

    def test_if_the_blind_single_tree_init_works(self):
        self.assertEqual(self.my_bst.value, None)
        self.assertEqual(self.my_bst.right, None)
        self.assertEqual(self.my_bst.left, None)

    def test_the_insert_function(self):
        self.my_bst.insert(5)
        self.assertEqual(self.my_bst.value, 5)

    def test_inserting_subtrees_left_and_right(self):
        self.my_bst.insert(5)
        self.my_bst.insert(3)
        self.assertEqual(self.my_bst.left.value, 3)
        self.my_bst.insert(6)
        self.assertEqual(self.my_bst.right.value, 6)
        #now to make sure there's no ghost data hanging around.
        self.assertIsNone(self.my_bst.right.left)
        self.assertIsNone(self.my_bst.right.right)

    def test_filling_up_a_tree(self):
        self.my_bst.insert(5)
        self.my_bst.insert(3)
        self.my_bst.insert(6)
        self.my_bst.insert(8)
        self.my_bst.insert(11)
        self.my_bst.insert(2)
        self.assertEqual(self.my_bst.left.value, 3)
        self.assertEqual(self.my_bst.left.left.value, 2)
        self.assertEqual(self.my_bst.right.value, 6)
        self.assertEqual(self.my_bst.right.right.value, 8)
        self.assertEqual(self.my_bst.right.right.right.value, 11)

class TestingMyMethods(unittest.TestCase):
    """Now let's test the methods"""
    def setUp(self):
        self.my_bst = BSTree()
        self.filled_tree = BSTree()
        self.filled_tree.insert(5)
        self.filled_tree.insert(3)
        self.filled_tree.insert(6)
        self.filled_tree.insert(8)
        self.filled_tree.insert(11)
        self.filled_tree.insert(2)

    def test_the_contains_method_on_empty_tree(self):
        self.assertEqual(self.my_bst.contains(5), False)

    def test_contains_on_tree_that_doesnt_have_the_val(self):
        self.assertEqual(self.filled_tree.contains(1), False)

    def test_contains_for_values_it_has(self):
        self.assertEqual(self.filled_tree.contains(8), True)
        self.assertEqual(self.filled_tree.contains(2), True)
        self.assertEqual(self.filled_tree.contains(5), True)
        self.assertEqual(self.filled_tree.contains(11), True)
        self.assertEqual(self.filled_tree.contains(6), True)
        self.assertEqual(self.filled_tree.contains(3), True)

    def test_size(self):
        self.assertEqual(self.my_bst.size(), 0)
        self.my_bst.insert(1)
        self.assertEqual(self.my_bst.size(), 1)
        self.assertEqual(self.filled_tree.size(), 35)
        self.filled_tree.insert(15)
        self.assertEqual(self.filled_tree.size(), 50)

    # def test_the_depth_method(self):
    #     self.assertEqual(self.my_bst.depth(), 0)
    #     self.assertEqual(self.filled_tree.depth(), 4)




if __name__ == '__main__':
    unittest.main()
