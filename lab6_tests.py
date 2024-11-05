import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1

    def test_selection_sort_books1(self):
        book_list1 = [Book("WS", "Macbeth"), Book("WS", "The Tempest"), Book("WS", "Midsummer Night's Dream"), Book("SK", "Merchant of Venice")]
        self.assertEqual(selection_sort_books(book_list1), ["Macbeth", "Merchant of Venice", "Midsummer Night's Dream", "The Tempest"])

    def test_selection_sort_books2(self):
        book_list1 = [Book("SK", "It"), Book("SK", "1963"), Book("SK", "Salem's Lot"), Book("SK", "Christine"), Book("SK", "The Shining"), Book("SK", "Misery")]
        self.assertEqual(selection_sort_books(book_list1),
                         ["1963", "Christine", "It", "Misery","Salem's Lot", "The Shining"])
    
        self.assertEqual(swap_case("Call me ISHMAL"), "cALL ME ishmal")
    


    # Part 2
    def test_swap_case1(self):
        self.assertEqual(swap_case("QwErTyUiOp"), "qWeRtYuIoP")
    def test_swap_case2(self):

    # Part 3
    def test_str_translate1(self):
        self.assertEqual(str_translate("banana pancakes", "a", "b"), "bbnbnb pbncbkes")
    def test_str_translate2(self):
        self.assertEqual(str_translate("assessment finished", "s", "t"), "attettment finithed")

    # Part 4
    def test_histogram1(self):
        self.assertEqual(histogram("how much wood would a wood chuck chuck if a wood chuck could chuck wood"),
                         {"how": 1, "much": 1, "wood": 4, "would": 1, "a": 2, "chuck": 4, "if": 1, "could": 1})
    def test_histogram2(self):
        self.assertEqual(histogram("robot car truck truck robot toy car car truck"),
                         {"robot": 2, "car": 3, "truck": 3, "toy": 1})




if __name__ == '__main__':
    unittest.main()
