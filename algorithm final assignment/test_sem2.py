from sem2 import *
import unittest

root = Tk()
app = main_window(root)


class TestSem2(unittest.TestCase):
    def test_sort(self):
        test_array = [(190013, 'rajeesha', 'thamel', '665526', 'Bsc. (Hons) Computing'),
                      (190046, 'shristi', 'nayabazar', '65799112', 'Bsc. (Hons) Ethical Hacking')]
        expected = [(190046, 'shristi', 'nayabazar', '65799112', 'Bsc. (Hons) Ethical Hacking'),
                    (190013, 'rajeesha', 'thamel', '665526', 'Bsc. (Hons) Computing')]
        app.quickSort(test_array, 0, len(test_array)-1)

        self.assertEqual(test_array, expected)

    def test_search(self):
        app.combo_search.set('Name')
        app.entry_search.insert(0, 'shristi')
        test_array = [(190013, 'rajeesha', 'thamel', '665526', 'Bsc. (Hons) Computing'),
                      (190046, 'shristi', 'nayabazar', '65799112', 'Bsc. (Hons) Ethical Hacking')]
        expected = [(190046, 'shristi', 'nayabazar', '65799112', 'Bsc. (Hons) Ethical Hacking')]
        actual_result = app.search_all(test_array)

        self.assertEqual(actual_result, expected)


