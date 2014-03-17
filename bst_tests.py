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
        self.my_bst.insert(5)
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
        self.assertEqual(self.filled_tree.contains(9), False)

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
        self.assertEqual(self.filled_tree.size(), 6)
        self.filled_tree.insert(15)
        self.assertEqual(self.filled_tree.size(), 7)

    def test_the_depth_method(self):
        self.assertEqual(self.my_bst.depth(), 0)
        self.assertEqual(self.filled_tree.depth(), 4)
        self.filled_tree.insert(5422)
        self.assertEqual(self.filled_tree.depth(), 5)

    def test_balance(self):
        self.assertEqual(self.my_bst.balance(), 0)
        self.assertEqual(self.filled_tree.balance(), 1)
        self.filled_tree.insert(5422)
        self.assertEqual(self.filled_tree.balance(), 2)


class testInOrder(unittest.TestCase):

    def setUp(self):
        self.my_bst = BSTree()
        self.filled_tree = BSTree()
        self.filled_tree.insert(5)
        self.filled_tree.insert(3)
        self.filled_tree.insert(6)
        self.filled_tree.insert(8)
        self.filled_tree.insert(11)
        self.filled_tree.insert(2)
        self.filled_tree.insert(9)
        # i just realized how unbalanced that tree is. bad design on my part.
        # i'll fix it for the following.
        self.number_catcher = []

    def test_in_order_on_empty_bst(self):
        for i in self.my_bst.in_order():
            self.number_catcher.append(i)
        self.assertEqual(self.number_catcher, [None])

    def test_in_order_on_filled_bst(self):
        for i in self.filled_tree.in_order():
            self.number_catcher.append(i)
        self.assertEqual(self.number_catcher, [2, 3, 5, 6, 8, 9, 11])


class testPrePostAndBreadth(unittest.TestCase):

    def setUp(self):
        self.my_bst = BSTree()
        self.filled_tree = BSTree()
        self.filled_tree.insert(10)
        self.filled_tree.insert(5)
        self.filled_tree.insert(15)
        self.filled_tree.insert(2)
        self.filled_tree.insert(12)
        self.filled_tree.insert(7)
        self.filled_tree.insert(17)
        self.filled_tree.insert(1)
        self.filled_tree.insert(4)
        self.filled_tree.insert(6)
        self.filled_tree.insert(9)
        self.filled_tree.insert(11)
        self.filled_tree.insert(14)
        self.filled_tree.insert(16)
        self.filled_tree.insert(23)
        self.number_catcher = []

    def test_pre_order_on_empty_bst(self):
        for i in self.my_bst.pre_order():
            self.number_catcher.append(i)
        self.assertEqual(self.number_catcher, [])

    def test_pre_order_on_filled_bst(self):
        for i in self.filled_tree.pre_order():
            self.number_catcher.append(i)
        self.assertEqual(self.number_catcher, [10, 5, 2, 1, 4, 7, 6, 9,
                                               15, 12, 11, 14, 17, 16,
                                               23])

    def test_post_order_on_empty_bst(self):
        for i in self.my_bst.post_order():
            self.number_catcher.append(i)
        self.assertEqual(self.number_catcher, [])

    def test_post_order_on_filled_bst(self):
        for i in self.filled_tree.post_order():
            self.number_catcher.append(i)
        self.assertEqual(self.number_catcher, [1, 4, 2, 6, 9, 7, 5, 11, 14, 12,
                                               16, 23, 17, 15, 10])

    def test_breadth_first_on_empty(self):
        for i in self.my_bst.breadth_first():
            self.number_catcher.append(i)
        self.assertEqual(self.number_catcher, [])
        pass

    def test_breadth_first_on_filled(self):
        for i in self.filled_tree.breadth_first():
            self.number_catcher.append(i)
        self.assertEqual(self.number_catcher, [10, 5, 15, 2, 7, 12, 17, 1, 4,
                                               6, 9, 11, 14, 16, 23])

    def testing_the_delete_message(self):
        pass


if __name__ == '__main__':
    unittest.main()
